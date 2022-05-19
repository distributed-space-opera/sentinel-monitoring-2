import grpc
import master_comm_pb2
import master_comm_pb2_grpc

# MASTER_HOST =  "ec2-18-189-2-173.us-east-2.compute.amazonaws.com"
MASTER_HOST = "192.168.43.177" # ROUNAK
# MASTER_HOST = "192.168.1.159" # MAYANK
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
        try:
            print('Get list of nodes from master')
            request = master_comm_pb2.GetListOfNodesRequest()
            # return ["192.168.220.175"]
            nodes = self.stub.GetListOfNodes(request)
            print("Node ips ", nodes.nodeips)
            return nodes.nodeips
        except Exception as e:
            print("Cant fetch list of nodes from master" + str(e))
            return []

    def updateNodeDown(self, ip):
        request = master_comm_pb2.NodeDownUpdateRequest(nodeip = ip)
        response = self.stub.NodeDownUpdate(request)
        print("Master down update response ", response)
        return response

if __name__ == '__main__':
    client = MasterClient()
    result = client.getAllNodes()
    print(f'{result}')