import socket

HOST = socket.gethostname()
PORT = 1241
HEADER_SIZE = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:

        full_msg = ""
        new_msg = True

        # continue receiving data until we get the total message
        while True:
            data = s.recv(16)

            # read the header here for any new message
            if new_msg:
                msg_len = int(data[:HEADER_SIZE])
                new_msg = False

            # appending to the full message
            full_msg += data.decode("utf-8")

            # when we read the full message
            print(len(full_msg) - HEADER_SIZE, msg_len)
            if len(full_msg) - HEADER_SIZE == msg_len:
                print("Full message received")
                print(f"The message is: {full_msg[HEADER_SIZE:]}")
                new_msg = True
                full_msg = ''   # resetting the full message
        
        