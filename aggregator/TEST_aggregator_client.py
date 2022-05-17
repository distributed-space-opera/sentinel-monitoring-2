import grpc
import aggregator_pb2;
import aggregator_pb2_grpc;
from datetime import datetime;
import time;

HOST = 'localhost'
PORT = 50052

class TESTAggregatorClient():
    def __init__(self):
        self.host = HOST
        self.server_port = PORT
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))
            
        self.stub = aggregator_pb2_grpc.AggregatorServiceStub(self.channel)


    def sendData(self, node_status_obj):

        while (True):
            request = aggregator_pb2.PersistableHeartBeat(**node_status_obj)
            response = self.stub.PersistHeartBeat(request)
            print("Monitor Server Response: " + str(response))
            print("ACK from Monitor: " + str(response.ACK))
            time.sleep(1)

if __name__ == '__main__':
    client = TESTAggregatorClient()
    node_status_desc = {
        'node_ip': '127.0.0.1',
        'node_status': 'UP',
        'timestamp': str(datetime.now()),
        'response_time': '0.01' 
    }
    # ack = client.sendDataToAggregator(node_status_desc)
    client.sendData(node_status_desc)