import socket
import pickle

HEADER_SIZE: int = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 8888))

    full_msg = b''
    new_msg = True
    while True:

        # receives the data in the chunks
        data = s.recv(16)

        if not data:
            break

        if new_msg:
            # receiving message's actual length
            msg_len = int(data[:HEADER_SIZE])

            # tagging that the message is now old, and not enter this if condtn
            new_msg = False

        # appending the chunks in the full_msg variable
        full_msg += data

        # until we iterate the full message
        if len(full_msg) - HEADER_SIZE == msg_len:
            
            # full message received
            print("Full message received!!!")
            b_obj: bytes = full_msg[HEADER_SIZE:]
            
            p_obj = pickle.loads(b_obj)
            print(p_obj)

            new_msg = True
            full_msg = ''
        