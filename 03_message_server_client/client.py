import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 8888  # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter your message >> ")
        s.send(message.encode())
        data = s.recv(1024).decode()
        if message.lower() == 'quit' or data.lower() == 'quit':
            break
        print(f"Received message from server: {data}")
