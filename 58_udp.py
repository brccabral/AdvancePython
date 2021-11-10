# UDP - User Datagram Protocol

import multiprocessing
import threading
import socket
import sys
import time
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    

# one process is broadcaster
# one process is listener

# Socket
def make_socket(ip='localhost', port=2045, sender=False):
    proc = multiprocessing.current_process().name
    logging.info(f'{proc} starting')

    address = (ip, port)
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    if sender:
        logging.info(f'{proc} starting to send')
    else:
        logging.info(f'{proc} binding to port')
        s.bind(address)
    
    with s:
        while True:
            if sender:
                logging.info(f'{proc}: sending...')
                s.sendto(b'Hello UDP', address)
                time.sleep(1)
            else:
                data, addr = s.recvfrom(1024) # blocking thread
                logging.info(f'{proc}" from {addr} = {data}')
    
def main():
    logging.info(f'Main start')
    broadcaster = multiprocessing.Process(target=make_socket, kwargs={'sender': True}, daemon=True, name='Broadcaster')
    listener = multiprocessing.Process(target=make_socket, kwargs={'sender': False}, daemon=True, name='Listener')

    broadcaster.start()
    listener.start()

    # run the Main for 5 seconds and exit()
    timer = threading.Timer(5, sys.exit, [0])
    timer.start()
    timer.join()
    
    logging.info(f'Main finish')

if __name__ == "__main__":
    main()