# pool of process and their results

import logging
import multiprocessing
from multiprocessing.context import Process
import time
import random

def work(item, count):
    name = multiprocessing.current_process().name
    logging.info(f'{name=} {item=} {count=} started')
    for x in range(count):
        logging.info(f'{name=} {item=} {count=} {x=}')
        time.sleep(1)
    logging.info(f'{name=} {item=} {count=} finished')
    # if exitcode is 0 (terminates normally), worker returns this message
    return f'{name=} {item=} {count=} is finished'

# callback function
def proc_result(result):
    logging.info(f'Result: {result=}')


def main():
    logging.info(f'Main started')

    max_ = 5
    pool = multiprocessing.Pool(max_)
    results = []
    for x in range(max_):
        item = f'Item {x}'
        # this random will make workers end out of order
        count = random.randrange(1, 5)
        r = pool.apply_async(func=work, args=[item, count], callback=proc_result)
        # messages will be out of order
        results.append(r)
    
    # wait for processes
    for r in results:
        r.wait()
    
    # pool.close() or pool.terminate()
    pool.close()
    pool.join()
    
    logging.info(f'Main finished')

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    
if __name__ == "__main__":
    main()