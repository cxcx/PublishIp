import socket

def create_server(port = 2409):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(128)

    return sock

def main():
    sock = create_server()
    while True:
        (connect_sock, addr) = sock.accept()
        if addr is not None:
            print(addr)
        connect_sock.close()

if __name__ == '__main__':
    main()
