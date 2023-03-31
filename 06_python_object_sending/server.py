import socket
import pickle

HEADER_SIZE: int = 10

# python object
p_obj = {
    "First Name": "Subhranil",
    "Second Name": "Sarkar"
}

def add_header(msg: bytes):
    return bytes(f"{len(msg):<{HEADER_SIZE}}", encoding="utf-8") + msg

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 8888))
    s.listen(5)

    conn, addr = s.accept()

    with conn:
        print(f"Connected by: {addr}")

        data = pickle.dumps(p_obj)
        data = add_header(data)

        conn.send(data)
