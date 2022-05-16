import grpc
from concurrent import futures
import time
import alert_manager_pb2 as pb2
import alert_manager_pb2_grpc as pb2_grpc


class AlertManagerService(pb2_grpc.AlertManagerServiceServicer):

    def __init__(self, *args, **kwargs):
        pass

    def NodeDown(self, request, context):
        message = request.nodeIP
        # result = f'Hello I am up and running received "{message}" message from you'
        print(message)
        result = {'responseCode': 200, 'responseMessage': "OK"}

        return pb2.NodeStatusResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_AlertManagerServiceServicer_to_server(AlertManagerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()