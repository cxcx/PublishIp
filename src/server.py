import socket
import redis

addr = '' 
r = None

def create_server(port = 2409):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    sock.bind(("", port))
    sock.listen(128)

    return sock

def main():
    sock = create_server()
    global addr
    global r
    while True:
        (connect_sock, remote) = sock.accept()
        if remote is not None and remote[0] != addr:
            print(remote)
            addr = remote[0]
            if r is None:
                r = redis.Redis()
            r.set('addr', addr)
        connect_sock.close()

if __name__ == '__main__':
    main()