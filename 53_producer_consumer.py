# demonstrates queue and event with locks
# producer in one thread, consumer in another thread

import random
import threading
import multiprocessing
from threading import Thread
from queue import Queue
import time
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    

def display(msg):
    thredname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname}\\{thredname}: {msg}')

# Producer
def create_work(queue: Queue, finished: Queue, max_: int):
    # finished is going to replace locking
    finished.put(False)
    for x in range(max_):
        time.sleep(random.random())
        v = random.randint(1, 100)
        queue.put(v)
        display(f'Producing: {x}: {v}')
    finished.put(True)
    display(f'Producing finished')

# Consumer
def perform_work(work: Queue, finished: Queue):
    counter = 0
    while True: # wait until break condition, which is given by finished from create_work
        if not work.empty(): # will be empty until queue.put(v) from create_work, and when all work.get() have been taken
            time.sleep(random.random())
            v = work.get() # get next item in queue and removes from work queue
            display(f'Consuming {counter}: {v}')
            counter += 1
        else:
            if not finished.empty():
                q = finished.get()
            else:
                q = False
            if q == True and work.empty(): # need to compare to True, otherwise it will return some value and break
                break
    display('Consuming finished')

def main():
    display('Main started')
    max_ = 50
    work = Queue()
    finished = Queue()
    finished.put(False)

    # producer will generate numbers in order 1,2,3,4
    # and consumer will get them in same order
    producer = Thread(target=create_work, args=[work, finished, max_], daemon=True)
    consumer = Thread(target=perform_work, args=[work, finished], daemon=True)

    producer.start()
    consumer.start()

    producer.join()
    display('Producer has finished')

    consumer.join()
    display('Consumer has finished')

    display('Main finished')


if __name__ == "__main__":
    main()