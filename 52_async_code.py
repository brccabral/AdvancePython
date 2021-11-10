# asunc runs in the same thread
# async uses CoRoutines which run on the same thread
# we also introduce the "async" and "await" keywords

# it uses time slots in between cpu calls

import threading
import multiprocessing
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    
import asyncio
import random

# functions
def display(msg):
    thredname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname}\\{thredname}: {msg}')

# tell python this funtion can be run async
# it doesn't need to be, but it can
async def work(name):
    # the work will start in given order, but will end 
    # in different order depending on rand_sleep
    rand_sleep = random.randint(1, 10)
    display(f'{name} started {rand_sleep=}')
    # do something
    # the work() is async, but here we need to wait
    # for the asynio() to return
    await asyncio.sleep(rand_sleep)
    display(f'{name} finished {rand_sleep=}')

async def run_async(max_):
    tasks = []
    for x in range(max_):
        name = f'Item {x}'
        tasks.append(asyncio.ensure_future(work(name)))
    # wait for all tasks to complete
    await asyncio.gather(*tasks)

def main():
    display('Main started')

    loop = asyncio.get_event_loop()
    
    # loop.run_forever() # used for long running programs (webserver, database)
    
    # run_until_complete() asks for a future
    # a future is an async with await
    loop.run_until_complete(run_async(50))

    loop.close() # free up resources


    display('Main finished')


if __name__ == "__main__":
    main()