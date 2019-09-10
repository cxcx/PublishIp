import socket
import time

def connect_server(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
    except socket.error as e:
        if e is not None:
            raise e
    s.close()

if __name__ == '__main__':
    while True:
        connect_server("", )
        time.sleep(2)
