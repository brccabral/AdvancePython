# avoid dreaded race conditions and deadlocks
# Race condition: same resource modified by multiple threads
#   one thread changes one value but the next thread was expeting the old value
# Deadlock: multiple threads waiting on the same resource
#   one thread locks the resource but doesn't unlock it, the other
#   threads will keep waiting forever

import logging
import threading
from concurrent.futures import ThreadPoolExecutor # Python >= 3.2
import time
import random

counter = 0 # global variable, all threads will try to access it

def test(step):
    global counter
    threadname = threading.currentThread().name
    logging.info(f'Starting {threadname}')

    for x in range(step):
        logging.info(f'Step: {threadname} += {step} {x=}')

        # the global interpreter lock (GIL) in action
        # counter += 1

        # Locking
        # lock = threading.Lock()
        # lock.acquire()
        # # lock.acquire() # deadlock - waiting on resources
        # try:
        #     # change the global variable inside a lock()
        #     counter += 1
        # finally:
        #     lock.release()

        # Locking simplified
        lock = threading.Lock()
        with lock: # this will auto-release the lock\
            logging.info(f'Locked: {threadname}')
            # change the global variable inside a lock()
            counter += 1
            time.sleep(2)

    logging.info(f'Counter {threadname} {counter}')
    logging.info(f'Completed {threadname}')
    

def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Starting')

    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for x in range(workers*2):
            step = random.randrange(1, 5)
            executor.submit(test, step)
    
    logging.info('App Finished')


if __name__ == "__main__":
    main()