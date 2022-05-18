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

def sendDataToAgg(ip, status, responsetime):
    node_status_desc = {
        'node_ip': ip,
        'node_status': 'UP' if status else 'DOWN',
        'timestamp': str(datetime.now()),
        'response_time': str(responsetime) 
    }
    try:
        aggregatorClient.sendData(node_status_obj=node_status_desc)
    except:
        print("Can't connect to Aggregator")


def notifyMaster(ip):
    try:
        masterClient.updateNodeDown(ip)
    except:
        print("Can't connect to Master to update node down status")


def notifyAlertManager(ip):
    try:
        alertManagerClient.notifyNodeDown(ip)
    except:
        print("Can't connect to Alert manager")

# {ip : [time_elapsed, next_check_time]}
expo_backoff = {}

def set_expo_backoff(ip):
    if ip in expo_backoff:
        expo_backoff[ip][1] = 2 * expo_backoff[ip][1]
    else:
        expo_backoff[ip] = [0, 1]

def should_check(ip):
    if ip in expo_backoff:
        expo_backoff[ip][0] =  (expo_backoff[ip][0] + 1)
        if expo_backoff[ip][0] == expo_backoff[ip][1]:
            return True
        else: 
            return False
    else:
        return True

def check_nodes_health(nodes):
    for node in nodes:
        ip = node.split(":")[0]
        port = 3000 # node.split(":")[1]
        health_check_success = True

        check = should_check(ip)
        print(expo_backoff, ip, check);

        if not check:
            continue

        try:
            # Check health of node
            starttime = datetime.now()
            nodeClient = sentinel_node_client.NodeClient(ip, port)
            status = nodeClient.checkHealth()
            endtime = datetime.now()
            expo_backoff.pop(ip, None)
            print(status)
            sendDataToAgg(ip, health_check_success, '%.3f' % ((endtime - starttime).total_seconds() * 1000))
        except:
            set_expo_backoff(ip)

            if expo_backoff[ip][0] == 8:
                health_check_success = False

                print("Mark node as down", ip)
                expo_backoff.pop(ip, None)

                # notify master
                notifyMaster(ip)

                # notify alert manager. check if not notified within past 5 mins
                notifyAlertManager(ip)

                sendDataToAgg(ip, health_check_success, 'NA')
            else:
                sendDataToAgg(ip, True, 'NA')
            
if __name__ == '__main__':
    start()

