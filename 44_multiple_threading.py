import logging
from threading import Thread
import time
import random

# funtion that will perform work

def long_task(name):
    max_ = random.randrange(1, 10)
    logging.info(f'Task: {name} performing {max_} times')
    for x in range(max_):
        logging.info(f'Task {name}: {x}')
        time.sleep(random.randrange(1, 3))
    logging.info(f'Task {name}: complete')

def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Starting')
    # long_task('main') # only this will run in the main thread and will take a long time

    # running multiple threads
    threads = []
    for x in range(10):
        t = Thread(target=long_task, args=[f'Thread {x}'])
        threads.append(t)
        t.start()
    
    # wait for all threads to finish
    # without this, the phrase "Finished all threads" is printed at the beginning
    # the join() makes the main thread to wait until all is finished
    for t in threads:
        t.join()

    logging.info('Finished all threads')

if __name__ == "__main__":
    main()