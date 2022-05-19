import grpc
import sentinel_comm_pb2
import sentinel_comm_pb2_grpc
import random

class NodeClient(object):
    def __init__(self, host, port):
        print(host, port)
        self.host = host
        self.server_port = port

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = sentinel_comm_pb2_grpc.SentinelMonitoringStub(self.channel)

    def checkHealth(self):
        request = sentinel_comm_pb2.healthCheckRequest()
        
        # c = random.choice(["OK", "FAIL"])
        # if c == 'FAIL': raise Exception("Error") 
        # return "OK"
        
        response = self.stub.healthCheck(request, timeout = 1)
        print('resss',response)
        return response

if __name__ == '__main__':
    client = NodeClient("localhost", 5055)
    result = client.checkHealth()
    print(f'{result}')