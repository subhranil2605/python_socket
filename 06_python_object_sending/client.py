import socket
import pickle

HEADER_SIZE: int = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 8888))
    data = s.recv(1024)
    
    obj = data[HEADER_SIZE:]
    obj = pickle.loads(obj)
    print(obj)