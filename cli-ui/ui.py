from threading import Thread
from prettytable import PrettyTable
import aggregator_client
import curses


aggregatorClient = aggregator_client.AggregatorClient()
screen = curses.initscr()

def startUI():
    t = Thread(target=refresh)
    t.start()

def refresh():
    ''' every 1 second '''
    while True:
        x = PrettyTable()
        x.field_names = ["Instance IP", " Status ", " Time checked at ", " Ping time"]
        allNodesHealth  = aggregatorClient.getAllNodesHealth()


        try:
            iterator = iter(allNodesHealth)
        except:
            screen.clear()
            screen.addstr(0, 0, 'Cannot communicate to aggregator')
            screen.refresh()
            curses.napms(1000)
            continue
        
        for nodeHealth in allNodesHealth:
            x.add_row([nodeHealth.node_ip, nodeHealth.node_status, nodeHealth.timestamp, nodeHealth.response_time])
        screen.addstr(0, 0, str(x))
        screen.refresh()
        curses.napms(1000)
        # curses.endwin()


if __name__ == '__main__':
    startUI()