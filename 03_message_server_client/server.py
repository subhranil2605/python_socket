import socket

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print('Waiting for a client to connect...')
    conn, addr = s.accept()
    print(f'Client connected: {addr}')
    with conn:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            print(f"Received message from the client: {data}")

            message = input("Enter your response >> ")
            conn.send(message.encode())
            
            if data.lower() == 'quit' or message.lower() == 'quit':
                break
