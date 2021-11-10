import logging
import multiprocessing
from multiprocessing.context import Process
import time

# worker action
def work(msg, max_):
    name = multiprocessing.current_process().name
    logging.info(f'{name} started')
    for x in range(max_):
        logging.info(f'{name} {msg}')
        time.sleep(1)
    logging.info(f'{name} finished')


# Main process

def main():
    logging.info(f'Main started')
    
    # if sleep() < max_ , it means that main stops
    # before worker, so, worker will be terminated
    # and exitcode=15
    # if sleep() > max_ , worker will end normally
    # exitcode=0 and then main will end

    max_ = 2
    worker = Process(target=work, args=['Working', max_], daemon=True, name='Worker')
    worker.start()
    
    time.sleep(5)

    # if the process is running, stop it
    if worker.is_alive():
        worker.terminate()
    worker.join()
    
    logging.info(f'Main finished {worker.exitcode=}')

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    
if __name__ == "__main__":
    main()