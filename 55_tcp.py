
import socket
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    

# TCP Client
def download(server, port):
    # family = socket.AF_INET - AF = Address Family
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    address = (server, port)
    logging.info(f'Connecting to {server}:{port}')

    s.connect(address) # three handshake (Ack)
    logging.info(f'Connected')

    logging.info(f'Send')
    s.send(b'Hello\r\n')
    
    logging.info(f'Receive')
    # recv() will block the thread and wait until receive something
    data = s.recv(1024) # avoid buffer overflow

    logging.info(f'Closing')
    s.close()

    logging.info(f'Data: {data}')



def main():
    logging.info(f'Main started')
    
    # download('voidrealms.com', 80) # 400 Bad Request
    # download('voidrealms.com', 7346) # ConnectionRefusedError: [Errno 111] Connection refused
    # download('bbbbbcajrjjbske.com', 7346) # socket.gaierror: [Errno -2] Name or service not known
    # download('youtube.com', 80) # 400 Bad Request
    
    logging.info(f'Main finished')


if __name__ == "__main__":
    main()
