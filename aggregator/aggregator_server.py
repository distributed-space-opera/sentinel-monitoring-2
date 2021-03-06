import grpc
import redis
import aggregator_pb2;
import aggregator_pb2_grpc;
from concurrent import futures;
import json
from google.protobuf.json_format import MessageToDict


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_KEY_HEALTH_STATUS_SUBSTRING = "_HEALTH_STATUS"

class AggregatorService(aggregator_pb2_grpc.AggregatorServiceServicer):

    def __init__(self):
        self.redisClient = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, charset="utf-8", decode_responses=True)
        print('Redis client at ' + REDIS_HOST + ":" + str(REDIS_PORT) + " initialized")
        self.redisClient.flushdb()


    def getNodeUpdates(self):
        allKeys = self.redisClient.keys('*_HEALTH_STATUS')

        nodeUpdates = []
        for key in allKeys:
            nodeRecentStatus = (self.redisClient.lrange(key, -1, -1))[0]
            nodeUpdates.append(nodeRecentStatus)

        return nodeUpdates


    def persistToRedis(self, node_status_obj):
        redisKey = node_status_obj.node_ip + REDIS_KEY_HEALTH_STATUS_SUBSTRING
        dict_msg = MessageToDict(node_status_obj)
        self.redisClient.rpush(redisKey, json.dumps(dict_msg))
        print('Presisted Heartbeat at redis key: {}'.format(redisKey))

    def PeristHeartBeat(self, request, context):
        # message = 'Heartbeat received ' + ' for IP: ' + request.node_ip + ' | Status: ' + request.node_status
        message = 'Heartbeat received ' + ' for IP: ' + request.node_ip + ' | Heartbeat: ' + str(request)
        print(message + "\n")
        print('Persisting heartbeat to redis')
        
        # persist this heartbeat in redis
        print(type(request))
        self.persistToRedis(request)



        print('------------------------------------------------------------------------------------------------\n')
        result = {
            'ACK': message
        }

        nodeUpdates = self.getNodeUpdates()
        print('\n\n ### All node updates: ')
        # print(nodeUpdates)
        for n in nodeUpdates:
            print(n)

        return aggregator_pb2.HeartBeatPersistedACK(**result)


    def GetAllNodesHealth(self, request, context):
        print('Call to grpc api GetAllNodesHealth received')
        allNodesHealthPyList = self.getNodeUpdates()

        res = aggregator_pb2.AllNodesHealthResponse()

        allNodesHealthResponse = aggregator_pb2.AllNodesHealthResponse()
        for nodeHealth in allNodesHealthPyList:
            obj = json.loads(nodeHealth)
            tempNodeHealthResponse = aggregator_pb2.PersistableHeartBeat(
                node_ip = obj['nodeIp'],
                node_status = obj['nodeStatus'],
                timestamp = obj['timestamp'],
                response_time = obj['responseTime']
            )
            allNodesHealthResponse.allNodesHealth.append(tempNodeHealthResponse)


        return allNodesHealthResponse

        # key * with substring HEALTH_STATUS - to get all nodes

            # for each
                # get the latest entry in redis, using lrange command
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    aggregator_pb2_grpc.add_AggregatorServiceServicer_to_server(AggregatorService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('Aggregator Server started')
    serve()
    