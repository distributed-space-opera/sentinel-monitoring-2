import grpc
import alert_manager_pb2 as pb2
import alert_manager_pb2_grpc as pb2_grpc


class AlertManagerClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.AlertManagerServiceStub(self.channel)

    def notifyNodeDown(self, nodeIP):
        request = pb2.NodeStatusRequest(nodeIP=nodeIP)
        return self.stub.NodeDown(request)


if __name__ == '__main__':
    client = AlertManagerClient()
    result = client.notifyNodeDown(nodeIP="10.1.1.1")
    print(f'{result}')