# reuse existing threads, because creating threads are expensive

import logging
import threading
from concurrent.futures import ThreadPoolExecutor # Python >= 3.2
import time
import random

# each thread will call this funtion
def test(item):
    s = random.randrange(1, 10)
    logging.info(f'Thread name {threading.current_thread().name} id {threading.get_ident()} item {item} start')
    logging.info(f'Thread name {threading.current_thread().name} item {item} sleeping for {s}')
    time.sleep(s)
    logging.info(f'Thread name {threading.current_thread().name} item {item} finished')

def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Starting')
    
    # there will be 5 workers
    # each worker will get one item and use it
    # after the item is finished, the worker will get a 
    # new item, until all items are finished
    # so, we have 5 threads and a queue of 15 items.
    workers = 5
    items = 15
    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(test, range(items))

    # the ThreadPoolExecutor auto joins main thread to wait
    # until all workers are done
    logging.info('Finished')


if __name__ == "__main__":
    main()