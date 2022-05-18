from urllib import response
import grpc
import aggregator_pb2;
import aggregator_pb2_grpc;
from datetime import datetime;
import time;

HOST = 'localhost'
PORT = 50052

class AggregatorClient():
    def __init__(self):

        self.a = 'Hello'

        self.host = HOST
        self.server_port = PORT

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = aggregator_pb2_grpc.AggregatorServiceStub(self.channel)


    def sendData(self, node_status_obj):
        print('self.a is: ' + self.a)

        while (True):
            request = aggregator_pb2.PersistableHeartBeat(**node_status_obj)
            response = self.stub.PeristHeartBeat(request)
            # print("Monitor Server Response: " + str(response))
            # print("ACK from Monitor: " + str(response.successACK))

            time.sleep(1)

    def getAllNodesHealth(self):
        request = aggregator_pb2.AllNodesHealthRequest()

        try:
            response = self.stub.GetAllNodesHealth(request)
        except:
            return aggregator_pb2.AllNodesHealthResponse()
        ## TODO: Remove hardcode
        # allNodesHealthResponse = aggregator_pb2.AllNodesHealthResponse()
        # for i in range(5):
        #     tempNodeHealthResponse = aggregator_pb2.PersistableHeartBeat()
        #     tempNodeHealthResponse.node_ip = '10.1.1.1'
        #     tempNodeHealthResponse.node_status = 'UP'
        #     tempNodeHealthResponse.timestamp = str(datetime.now())
        #     tempNodeHealthResponse.response_time = '0.01'
        #     allNodesHealthResponse.allNodesHealth.append(tempNodeHealthResponse)


        # allNodesHealth = []
        # for i in range (5):
        #     allNodesHealth.append({'node_ip': '127.0.0.1', 'node_status': 'UP', 'timestamp': str(datetime.now()),'response_time': '0.01' })
        # response = aggregator_pb2.AllNodesHealthResponse(allNodesHealth)

        # print("All nodes health response", response.allNodesHealth)
        return response.allNodesHealth

if __name__ == '__main__':
    client = AggregatorClient()
    node_status_desc = {
        'node_ip': '127.0.0.1',
        'node_status': 'UP',
        'timestamp': str(datetime.now()),
        'response_time': '0.01' 
    }
    # ack = client.sendDataToAggregator(node_status_desc)
    client.sendData(node_status_desc)