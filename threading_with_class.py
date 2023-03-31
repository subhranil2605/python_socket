import threading
import time


def my_work(desc):
    for i in range(10):
        print(f"{desc} >> {i}")
        time.sleep(1)


class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"Starting thread: {self.name}")
        my_work(self.name)
        print(f"Ending thread: {self.name}")

# ---------------------- Example 1 ----------------------
# # Create a MyThread object
# my_thread = MyThread(name="Thread 1")

# # start the thread
# my_thread.start()

# # wait for thread to finish
# my_thread.join()

# ---------------------- Example 2 ----------------------
threads = [MyThread(name=f"Thread {i + 1}") for i in range(5)]

# start all the threads
[thread.start() for thread in threads]

# wait for all threads to finish
[thread.join() for thread in threads]