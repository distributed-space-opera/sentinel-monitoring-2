from threading import Thread
import time
import alert_manager_client
import master_client

alertManagerClient = alert_manager_client.AlertManagerClient()
masterClient = master_client.MasterClient()

nodes = []

def start():
    '''Get list of all nodes from master'''
    global nodes
    nodes = masterClient.getAllNodes()
    t = Thread(target=heartbeat)
    t.start()

def heartbeat():
    ''' every 1 second '''
    while True:
        check_nodes_health()
        time.sleep(1)

def check_nodes_health():
    for node in nodes:
        print(node)
        '''
        // Check health of node

        // send data to aggregator

        if health check failed:
            // notify master

            // notify alert manager. check if not notified within past 5 mins
        '''
    
if __name__ == '__main__':
    start()