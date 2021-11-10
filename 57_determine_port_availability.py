
import socket
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)    

# check one port
def check_port(ip, port, timeout):
    ret = False
    logging.debug(f'Checking {ip}:{port}')

    try:
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        s.settimeout(timeout)
        con = s.connect_ex((ip, port)) # returns an integer that says if the connection was ok or fail
        logging.debug(f'Connection {ip}:{port} = {con}')
        s.close()

        if con == 0:
            ret = False
            logging.debug(f'In use {ip}:{port}')
        else:
            ret = True
            logging.debug(f'Usable {ip}:{port}')
        
    except Exception as e:
        ret = False
        logging.debug(f'Error {ip}:{port} = {e.msg}')
    finally:
        logging.debug(f'Returning {ip}:{port} = {ret}')
        return ret

# checking a range
def check_range(ip, scope):
    ret = {}
    for p in scope:
        r = check_port(ip, p, 1.0)
        ret[p] = r
    return ret

def main():
    # test one port
    p = check_port('localhost', 2594, 2.0)
    logging.info(f'Port 2594 usable: {p}')

    # test a range
    ## lsof | grep LISTEN
    ## ss -tulpn | grep LISTEN
    ## ss -tulpw | grep LISTEN
    ports = check_range('localhost', range(1710, 1720))
    for key, value in ports.items():
        logging.info(f'Port {key} usable {value}')
    

if __name__ == "__main__":
    main()