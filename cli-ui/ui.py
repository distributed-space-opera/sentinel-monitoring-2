from threading import Thread
from prettytable import PrettyTable
import aggregator_client
import curses
from datetime import datetime



aggregatorClient = aggregator_client.AggregatorClient()
screen = curses.initscr()

def startUI():
    t = Thread(target=refresh)
    t.start()

def refresh():
    ''' every 1 second '''
    while True:
        x = PrettyTable()
        x.field_names = ["Instance IP", " Ping time (ms)", " Status ", " Last checked "]
        


        try:
            allNodesHealth  = aggregatorClient.getAllNodesHealth()
            iterator = iter(allNodesHealth)
        except Exception as e:
            screen.clear()
            screen.addstr(0, 0, 'Cannot communicate to aggregator' + str(e))
            # print(e)
            screen.refresh()
            curses.napms(1000)
            continue
        
        for nodeHealth in allNodesHealth:
            dtobj = datetime.fromisoformat(nodeHealth.timestamp)
            delta =  datetime.now() - dtobj 
            x.add_row([nodeHealth.node_ip, nodeHealth.response_time, nodeHealth.node_status if (int(delta.total_seconds()) < 20) else 'UNKNOWN' , '{} second(s) ago.'.format(int(delta.total_seconds()))])
        screen.addstr(0, 0, str(x))
        screen.refresh()
        curses.napms(1000)
        # curses.endwin()


if __name__ == '__main__':
    startUI()