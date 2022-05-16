import grpc
import monitor_pb2;
import monitor_pb2_grpc;
import time;
from datetime import datetime

def run():
    while (True):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = monitor_pb2_grpc.MonitorStub(channel)
            node_status_desc = {
                'node_ip': '127.0.0.1',
                'node_status':'HEALTHY',
                'timestamp': str(datetime.now()),
                'response_time': '0.001'
            }
            response = stub.PersistHeartbeat(monitor_pb2.HeartBeat(**node_status_desc))
        print("Monitor Server Response: " + str(response))
        print("ACK from Monitor: " + str(response.successACK))

        time.sleep(1)
    

if __name__ == '__main__':
    print('Heartbeatsender started!')
    run()