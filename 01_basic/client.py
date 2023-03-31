import socket

HOST = socket.gethostname()
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

full_mssg = ''
while True:
    msg: bytes = s.recv(8)
    if len(msg) <= 0:
        break
    full_mssg += msg.decode("utf-8")

print(full_mssg)
