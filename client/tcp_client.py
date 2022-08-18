import socket
import sys


BUFFER_SIZE = 2048


def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print(f'connecting to {server_address}')
    sock.connect(server_address)

    try:

        # Send data
        message = 'This is the message.  It will be repeated.'
        print(f'sending "{message}"')
        sock.sendall(message.encode('utf-8'))

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(BUFFER_SIZE)
            amount_received += len(data)
            print(f'received "{data}"')

    finally:
        print('closing socket')
        sock.close()


if __name__ == '__main__':
    main()
