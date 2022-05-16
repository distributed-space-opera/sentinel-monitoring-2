import alert_manager
import master

alertManagerClient = alert_manager.AlertManagerClient()
masterClient = master.MasterClient()

def monitor():
    '''Get list of all nodes from master'''
    nodes = masterClient.getAllNodes()

    ''' every 1 second '''

    for node in nodes:
        '''
        // Check health of node

        // send data to aggregator

        if health check failed:
            // notify master

            // notify alert manager. check if not notified within past 5 mins
        '''
    
if __name__ == '__main__':
    monitor()