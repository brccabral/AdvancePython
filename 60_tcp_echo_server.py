# make a TCP server in a process that handles multiple clients
# echos back the data to the same client (not all clients)

import logging
import multiprocessing
import socket
import select
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    


# Server
def chat_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info(f'Binding to {ip}:{port}')
    server.bind((ip, port))
    server.setblocking(False)
    server.listen(100)
    logging.info(f'Listening on {ip}:{port}')
    
    readers = [server]

    while True:
        readable, writable, errored = select.select(readers, [], [], 0.5)

        s: socket.socket
        for s in readable:
            try:
                if s == server:
                    client, address = s.accept()
                    client.setblocking(False)
                    readers.append(client)
                    logging.info(f'Client Connection: {address}')
                else:
                    data = s.recv(1024)
                    if data:
                        logging.info(f'Echo: {data}')
                        s.send(data)
                    else:
                        logging.info(f'Remove: {s}')
                        s.close()
                        readers.remove(s)
            except Exception as e:
                logging.warning(f'{e.args}')
            finally:
                pass


def main():
    svr = multiprocessing.Process(target=chat_server, args=['localhost', 2067], daemon=True, name='Server')
    # connect the client using telnet
    ## telnet 127.0.0.1 2067
    # can connect multiple telnet clients
    
    while True:
        command = input('Enter a command (start, stop): ')
        if command == 'start':
            logging.info(f'Starting the server')
            svr.start()
        if command == 'stop':
            logging.info(f'Stopping ther server')
            svr.terminate()
            svr.join()
            svr.close()
            logging.info(f'Server Stopped')
            break
    
    logging.info(f'App finished')

if __name__ == "__main__":
    main()