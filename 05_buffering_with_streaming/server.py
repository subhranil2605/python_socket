import socket
import time

HOST = socket.gethostname()
PORT = 1241
HEADER_SIZE = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        client_socket, addr = s.accept()
        print(f"Connected by: {addr}")

        msg = "Welcome to the server! This is Subhranil Sarkar"
        msg = f"{len(msg):<{HEADER_SIZE}}" + msg

        client_socket.send(bytes(msg, "utf-8"))

        # continue to send data
        while True:
            time.sleep(2)
            msg = f"The time is: {time.time()}"
            msg = f"{len(msg):<{HEADER_SIZE}}" + msg

            client_socket.send(bytes(msg, "utf-8"))
