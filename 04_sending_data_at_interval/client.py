import socket
import time

HOST = "localhost"
PORT = 8888


def send_data(sock, data):
    sock.send(bytes(data, encoding="utf-8"))
    time.sleep(1)


def recv_data(sock):
    mssg = sock.recv(1024).decode()
    print(f"Received: {mssg}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to the server
    s.connect((HOST, PORT))

    i = 0
    while True:
        # send the data to the server
        send_data(s, str(i))

        # receive data from the server
        recv_data(s)
        i += 1
