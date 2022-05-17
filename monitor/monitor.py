from threading import Thread
import time
import alert_manager_client
import master_client
import sentinel_node_client
from datetime import datetime
import aggregator_client

alertManagerClient = alert_manager_client.AlertManagerClient()
masterClient = master_client.MasterClient()
aggregatorClient = aggregator_client.AggregatorClient()

def start():
    t = Thread(target=heartbeat)
    t.start()

def heartbeat():
    nodes = masterClient.getAllNodes()
    count = 0
    
    ''' every 1 second '''
    while True:
        if count == 5:
            '''Get list of all nodes from master every 5 seconds'''
            nodes = masterClient.getAllNodes()
            count = 0
            print('Node list refreshed', count)
        check_nodes_health(nodes)
        count+=1
        time.sleep(1)

def check_nodes_health(nodes):
    for node in nodes:
        ip = node.split(":")[0]
        port = node.split(":")[1]
        health_check_success = True

        try:
            # Check health of node
            nodeClient = sentinel_node_client.NodeClient(ip, port)
            status = nodeClient.checkHealth()
            print(status)
        except:
            health_check_success = False

            # notify master
            masterClient.updateNodeDown(ip)

            # notify alert manager. check if not notified within past 5 mins
            alertManagerClient.notifyNodeDown(ip)
    
        # send data to aggregator

if __name__ == '__main__':
    start()