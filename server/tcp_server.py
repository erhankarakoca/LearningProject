import socket
import sys


BUFFER_SIZE = 2048


def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)

    print(f'Starting the server on {server_address}')
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()

        try:
            print(f'connection from {client_address}')

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(BUFFER_SIZE)
                print(f'received "{data}"')
                if data:
                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print(f'no more data from {client_address}')
                    break

        finally:
            # Clean up the connection
            connection.close()


if __name__ == '__main__':
    main()
