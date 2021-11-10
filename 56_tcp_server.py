
import socket
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    

# TCP Server
def server(ip, port):
    # this is a blocking server
    # it will block the thred
    # not good for production
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    address = (ip, port)

    logging.info(f'Bind to {ip}:{port}')
    s.bind(address)

    logging.info(f'Listening')
    s.listen(1)

    con, addr = s.accept()
    logging.info(f'Connected: {addr}')

    while True:
        # recv() will block until receive something
        # use terminal and execute telnet to send data
        ## telnet ip port
        ## telnet 127.0.0.1 2607
        data = con.recv(1024)
        # if something is empty, close connection
        ## if using telnet, close terminal
        if len(data) == 0:
            logging.info(f'Exiting')
            con.close()
            break
        logging.info(f'Data: {data}')

    logging.info(f'Closing the server')
    s.close()
    

def main():
    logging.info(f'Main started')

    server('localhost', 2607) # above 1024

    logging.info(f'Main finished')


if __name__ == "__main__":
    main()
