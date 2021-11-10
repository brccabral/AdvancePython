# send and receive messages from/to threads

import logging
import time
import random
import threading
from threading import Thread
from concurrent.futures import ThreadPoolExecutor # Pyhton 3.2
from queue import Queue

# Queues
# Use queues to pass messages back and forths

# run the action
def test_que(name: str, que: Queue):
    threadname = threading.current_thread().name
    sleep_time = random.randrange(1, 5)
    logging.info(f'{threadname} Starting queue sleep for {sleep_time}')
    time.sleep(sleep_time) 
    logging.info(f'{threadname} Finished')
    return_msg = f'Hello {name} your random number is {random.randrange(1,10)}'
    que.put(return_msg) # saves message in que object


# creates the thread
def queued():
    que = Queue()
    t = Thread(target=test_que, args=['Bryan', que])
    t.start()
    logging.info('Do something on the main thread queued')
    t.join() # waits until test_que
    return_msg = que.get() # get the message created in the thread que
    logging.info(f'Returned {return_msg}')


# Futures
# use futures, easier and cleaner
def test_future(name: str):
    threadname = threading.current_thread().name
    sleep_time = random.randrange(1, 5)
    logging.info(f'{threadname} Starting future sleep for {sleep_time}')
    time.sleep(sleep_time)
    logging.info(f'{threadname} Finished')
    return_msg = f'Hello {name} your random number is {random.randrange(1,10)}'
    return return_msg

def pooled():
    workers = 20
    returned_msgs = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1,5)
            returned_future_msg = ex.submit(test_future, f'Bryan {x}')
            # the "returned_future_msg" doesn't exist yet
            # but we can already tell python what to do
            # it will append in order even if some threads
            # finish sooner
            returned_msgs.append(returned_future_msg)
    logging.info('Do something on the main thread futures')
    for r in returned_msgs:
        logging.info(f'Returned {r.result()}')


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Main thread Starting')
    queued()
    pooled()

    logging.info('Main thread Finished')


if __name__ == "__main__":
    main()
