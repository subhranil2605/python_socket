import socket 

HEADER_SIZE = 10

def add_header(msg: bytes):
    msg = f"{len(msg):<{HEADER_SIZE}}".encode() + msg
    return msg

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 8888))
    s.listen(5)
    print("Waiting for connections...")
    
    conn, addr = s.accept()

    with conn:
        print(f"Connected by: {addr}")

        message = b"Hello this is subhranil Sarkar"
        sent = conn.send(add_header(message))
        print(sent)
