from platform import node
import grpc
from concurrent import futures
import smtplib
import alert_manager_pb2 as pb2
import alert_manager_pb2_grpc as pb2_grpc
import email_service as EmailService


class AlertManagerService(pb2_grpc.AlertManagerServiceServicer):

    def __init__(self, *args, **kwargs):
        pass

    def NodeDown(self, request, context):
        nodeIP = request.nodeIP 
        print("Node down ", nodeIP)
        self.notifyByEmail(nodeIP)
        result = {'responseCode': 200, 'responseMessage': "OK"}

        return pb2.NodeStatusResponse(**result)

    def notifyByEmail(self, nodeIP):
        subject = 'Pager alert: Node %s is not responding' % nodeIP
        body = """\
            <html>
            <body>
                <p>Hi,<br>
                <p> The node instance with IP %s is not responding. Please take a look.</p>
            </body>
            </html>
            """ % nodeIP

        EmailService .sendEmail(subject, body)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_AlertManagerServiceServicer_to_server(AlertManagerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()