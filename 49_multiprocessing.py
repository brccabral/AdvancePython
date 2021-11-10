# multiple processes running the same script
# each process has its own memory space and its own threads

import logging
import multiprocessing
from multiprocessing import process
import time # will put each main process to sleep

def run(num):
    name = process.current_process().name
    logging.info(f'Run Running {name} as {__name__}')
    time.sleep(num*2)
    logging.info(f'Run Finished {name}')

# Basic process usage

def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    name = process.current_process().name
    logging.info(f'Main Running {name} as {__name__}')

    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=run, args=[x], daemon=True)
        processes.append(p)
        p.start()
    
    # wait for the process
    # if not, process 2,3,4 doesn't finish because the main
    # ends first and process 5 never gets the chance to start
    for p in processes:
        p.join()
    

    logging.info(f'Main Finished {name}')

if __name__ == "__main__":
    main()