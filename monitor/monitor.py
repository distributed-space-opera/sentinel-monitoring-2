from concurrent import futures

import grpc
import monitor_pb2;
import monitor_pb2_grpc;
import json

# instead of string node status - get an object
# persist the data to redis - make grpc call to Aggregator service

class Monitor(monitor_pb2_grpc.MonitorServicer):

    def PersistHeartbeat(self, request, context):
        # message = 'Heartbeat received ' + ' for IP: ' + request.node_status_desc.node_ip + ' | Status: ' + request.node_status_desc.node_status
        # message = 'Heartbeat received'
        message = 'Heartbeat received | ' + str(request)  #WORKS
        # message = 'Heartbeat received | ' + json.loads(str(request))

        # req = json.loads(request)
        # message = 'Heartbeat received ' + ' for IP: ' + request["node_status_desc.node_ip"] + ' | Status: ' + request["node_status_desc.node_status"]
        print(message)
        result = {
            'successACK': message
        }
        return monitor_pb2.HeartBeatReceivedACK(**result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    monitor_pb2_grpc.add_MonitorServicer_to_server(Monitor(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('main started')
    serve()