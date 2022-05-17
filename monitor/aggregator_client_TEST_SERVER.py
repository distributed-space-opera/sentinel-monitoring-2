import grpc
import aggregator_pb2;
import aggregator_pb2_grpc;
from concurrent import futures;

class AggregatorMOCK(aggregator_pb2_grpc.AggregatorClientServicer):

    def PeristHeartBeat(self, request, context):
            message = 'Heartbeat received ' + ' for IP: ' + request.node_ip + ' | Status: ' + request.node_status
            print(message)
            result = {
                'successACK': message
            }
            return aggregator_pb2.HeartBeatPersistedACK(**result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    aggregator_pb2_grpc.add_AggregatorClientServicer_to_server(AggregatorMOCK(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('main started')
    serve()
    