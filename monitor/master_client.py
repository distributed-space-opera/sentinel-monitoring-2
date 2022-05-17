import grpc
import master_comm_pb2
import master_comm_pb2_grpc

MASTER_HOST =  "ec2-3-134-115-89.us-east-2.compute.amazonaws.com"
MASTER_PORT = 6090

# MASTER_HOST =  "localhost"
# MASTER_PORT = 50051

class MasterClient(object):
    def __init__(self):
        self.host = MASTER_HOST
        self.server_port = MASTER_PORT

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = master_comm_pb2_grpc.ReplicationStub(self.channel)

    def getAllNodes(self):
        request = master_comm_pb2.GetListOfNodesRequest()
        return ["localhost:50051","localhost:50052"]
        # nodes = self.stub.GetListOfNodes(request)
        # print(nodes.nodeips)
        # return nodes.nodeips

    def updateNodeDown(self, ip):
        request = master_comm_pb2.NodeDownUpdateRequest(nodeip = ip)
        response = self.stub.NodeDownUpdate(request)
        print("Master down update response ", response)
        return response

if __name__ == '__main__':
    client = MasterClient()
    result = client.getAllNodes()
    print(f'{result}')