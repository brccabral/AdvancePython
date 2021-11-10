# communicate between process in the same or in other server

import random
import threading
import multiprocessing
from multiprocessing import process
from multiprocessing.context import Process
from multiprocessing.connection import Listener, Client
import time
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    

# Worker process
def proc(server='localhost', port=6000, password=b'password'):
    name = process.current_process().name
    logging.info(f'{name} started')

    # start listening for connections
    address = (server, port)
    listener = Listener(address=address, authkey=password)
    conn = listener.accept()
    logging.info(f'{name}: connection from {listener.last_accepted}')

    # loop for input
    while True:
        msg = conn.recv()
        logging.info(f'{name} data in: {msg}')
        if msg == 'quit':
            conn.close() # close the connection with client, but server is still up
            break
    
    listener.close() # close the server

    logging.info(f'{name} finished')


def main():
    name = process.current_process().name
    logging.info(f'{name} Main started')
    
    # setup the process
    server = 'localhost' # 127.0.0.1
    # lsof -i:2823
    # lsof -i -P -n | grep 2823
    # ss -tulpn | grep 2823
    # ss -tulpw | grep 2823
    port = 2823 # above 1024
    password = b'password'

    p = Process(target=proc, args=[server, port, password], daemon=True, name='Worker')
    p.start()

    logging.info(f'{name} waiting on the working...')
    time.sleep(1) # give time to start the listener and connections

    # connect to the process
    dest = (server, port)
    conn = Client(address=dest, authkey=password)

    # command loop
    while True:
        command = input('\r\nEnter a command or type quit:\r\n').strip()
        logging.info(f'{name} command: {command}')
        conn.send(command)
        if command == 'quit':
            break
    
    # cleanup and shutdown
    if p.is_alive():
        logging.info(f'{name} terminating worker')
        conn.close()
        time.sleep(1)
        p.terminate()
    p.join()

    logging.info(f'{name} Main finished')


if __name__ == "__main__":
    main()
