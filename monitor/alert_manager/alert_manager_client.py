import grpc
import alert_manager_pb2 as pb2
import alert_manager_pb2_grpc as pb2_grpc

ALERT_MANAGER_HOST = 'localhost'
ALERT_MANAGER_PORT = 50051

class AlertManagerClient(object):
    def __init__(self):
        self.host = ALERT_MANAGER_HOST
        self.server_port = ALERT_MANAGER_PORT

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = pb2_grpc.AlertManagerServiceStub(self.channel)

    def notifyNodeDown(self, nodeIP):
        request = pb2.NodeStatusRequest(nodeIP=nodeIP)

        print('request, 'f'{request}')
        return self.stub.NodeDown(request)


if __name__ == '__main__':
    client = AlertManagerClient()
    result = client.notifyNodeDown(nodeIP="10.1.1.1")
    print(f'{result}')