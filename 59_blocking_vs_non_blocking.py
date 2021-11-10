# block or not the thread the socket is running on

import logging
import socket
import select
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    

# select 
# This module supports asynchronous I/O on multiple file descriptors.
# *** IMPORTANT NOTICE ***
# On Windows, only sockets are supported; on Unix, all file descriptors.
## ready_to_read, ready_to_write, in_error = select.select(
#                                               potential_readers,
#                                               potential_writers,
#                                               potential_errs,
#                                               timeout
#                                               )

# blocking socket
def create_blocking(host, port):
    logging.info(f'Blocking - creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    logging.info(f'Blocking - connecting')
    s.connect((host, port))
    logging.info(f'Blocking - connected')
    
    logging.info(f'Blocking - sending...')
    s.send(b'hello\r\n')

    logging.info(f'Blocking - waiting...')
    data = s.recv(1024)
    logging.info(f'Blocking - data={len(data)}')
    logging.info(f'Blocking - closing...')
    s.close()

# non blocking socket example
# this is not for production environments
def create_nonblocking(host, port):
    logging.info(f'Non Blocking - creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    logging.info(f'Non Blocking - connecting')
    # check if can connect
    ret = s.connect_ex((host, port)) # this is BLOCKING
    if ret != 0:
        logging.info(f'Non Blocking - failed to connect')
        return
    
    logging.info(f'Non Blocking - connected')
    s.setblocking(False)

    inputs = [s]
    outputs = [s]

    # because we are working with http
    # send server info first and read back response
    while inputs: # while waiting for response
        logging.info(f'Non Blocking - waiting...')
        # we expect errors in input, not output
        # need the timeout to make it non blocking
        # every X timeout is going to try again
        ## the select is on background
        readable, writable, errors = select.select(inputs, outputs, inputs, 0.5)

        # null, writable, null
        for s in writable:
            logging.info(f'Non Blocking - sending...')
            data = s.send(b'hello\r\n') # returns number of bytes (int)
            logging.info(f'Non Blocking - sent: {data}')
            outputs.remove(s)
        
        # readable, null, null
        for s in readable:
            logging.info(f'Non Blocking - reading...')
            data = s.recv(1024)
            logging.info(f'Non Blocking - recv data: {len(data)}')
            logging.info(f'Non Blocking - closing...')
            s.close()
            inputs.remove(s)
            break
        
        for s in errors:
            logging.info(f'Non Blocking - error...')
            inputs.remove(s)
            outputs.remove(s)
            break
            

def main():
    logging.info(f'Main start')
    create_blocking('voidrealms.com', 80)
    create_nonblocking('voidrealms.com', 80)
    logging.info(f'Main finish')

if __name__ == "__main__":
    main()