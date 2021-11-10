# Quitting when we quit the app
# ctrl+c in the terminal or exit() kills the main thread, but not the 
# new threads, unless we use daemon=True
# daemon broadcast the quit to all threads

import logging
import threading
from concurrent.futures import ThreadPoolExecutor # Python >= 3.2
import time
import random
from threading import Timer, Thread


def test():
    threadname = threading.currentThread().name
    logging.info(f'{threadname} Starting')
    for x in range(60):
        logging.info(f'{threadname} Working')
        time.sleep(1)
    logging.info(f'{threadname} Finished')

def stop():
    logging.info('Exiting the app')
    exit(0)


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Main thread Starting')

    # stop in 3 seconds
    timer = Timer(3, stop)
    timer.start()

    # run a thread
    # t = Thread(target=test, daemon=False) # will run forever independent of main thread
    t = Thread(target=test, daemon=True) # quits all threads together with main
    t.start()

    logging.info('Main thread Finished')


if __name__ == "__main__":
    main()