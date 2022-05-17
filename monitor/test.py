from threading import Thread
import time

def heartbeat_tick():
    print('Hello')

def background_task():
    while True:
        heartbeat_tick()
        time.sleep(1)

t = Thread(target=background_task)
t.start()

