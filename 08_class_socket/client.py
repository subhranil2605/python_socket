import socket
from typing import Optional


HEADER_SIZE = 10


class MySocket:
    def __init__(self, sock=None):
        self.sock = sock or socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host: str, port: int):
        self.sock.connect((host, port))

    # def mysend(self, msg):
    #     totalsent = 0
    #     while totalsent < MSGLEN:
    #         sent = self.sock.send(msg[totalsent:])
    #         if sent == 0:
    #             raise RuntimeError("socket connection broken")
    #         totalsent += sent

    def myreceive(self):
        chunks = b""
        new_msg = True

        while True:
            buffer_size = 16
            chunk = self.sock.recv(buffer_size)

            if new_msg:
                msg_len = int(chunk[:HEADER_SIZE].strip())
                new_msg = False

            chunks += chunk
            if len(chunks) - HEADER_SIZE == msg_len:
                print("Full message received!!!")
                break

            if chunk == b'':
                raise RuntimeError("socket connection broken")
            
        return chunks[HEADER_SIZE:].decode()


client_socket = MySocket()
client_socket.connect(socket.gethostname(), 8888)
print(client_socket.myreceive())
