import grpc
import aggregator_pb2;
import aggregator_pb2_grpc;
from concurrent import futures;

class AggregatorService(aggregator_pb2_grpc.AggregatorServiceServicer):

    def PeristHeartBeat(self, request, context):
        # message = 'Heartbeat received ' + ' for IP: ' + request.node_ip + ' | Status: ' + request.node_status
        message = 'Heartbeat received ' + ' for IP: ' + request.node_ip + ' | Heartbeat: ' + str(request)
        print(message)
        print('------------------------------------------------------------------------------------------------\n')
        result = {
            'ACK': message
        }
        return aggregator_pb2.HeartBeatPersistedACK(**result)

    def GetAllNodesHealth(self, request, context):
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    aggregator_pb2_grpc.add_AggregatorServiceServicer_to_server(AggregatorService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('Aggregator Server started')
    serve()
    