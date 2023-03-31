import socket


HOST = "localhost"
PORT = 8888


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)

    conn, addr = s.accept()
    with conn:
        print(f"Connected by: {addr}")        

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            if len(data) > 0:
                print(f"Received Data from client: {data!r}")
            
            # sending back to the clients
            conn.sendall(f"(Server) >> Recieved from {addr} - {data}".encode())

