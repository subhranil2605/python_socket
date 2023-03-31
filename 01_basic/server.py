import socket

HOST = socket.gethostname()
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")
    client_socket.send(b"Welcome to the server!")
    client_socket.close()
