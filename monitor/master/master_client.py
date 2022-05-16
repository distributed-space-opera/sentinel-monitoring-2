import grpc
import master_comm_pb2
import master_comm_pb2_grpc

MASTER_HOST = 'localhost'
MASTER_PORT = 50051

class MasterClient(object):
    def __init__(self):
        self.host = MASTER_HOST
        self.server_port = MASTER_PORT

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = master_comm_pb2_grpc.ReplicationStub(self.channel)

    def getAllNodes(self):
        request = master_comm_pb2.GetListOfNodesRequest()

        print('request, 'f'{request}')
        return self.stub.GetListOfNodes(request)

if __name__ == '__main__':
    client = MasterClient()
    result = client.getAllNodes()
    print(f'{result}')