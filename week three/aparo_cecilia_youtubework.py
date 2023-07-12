# Remaining concepts in python

# context manager
# Multithreading and multiprocessing
# context manager -is an obj that defines a temporary context for a block of code

# example: demonstrate a context manager to open a file and returns a context manager instance

import multiprocessing
import threading
import time


def open_file(filename):
    '''open a file and return a context manager instance '''
    file = open(filename, "r")


def _enter_():
    return file


def _exit_(self, exc_type, exc_value, exc_tb):
    file.close()

    return _enter_, _exit_


with open_file("my_file.txt") as f:
    cotents = f.read()

# demonstrate context manager using a time series


class timer:
    def _enter_(self):
        self.start_time = time.time()

    def _exit_(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time - execution_time
        print(f"the time for this execution {execution_time} seconds elapsed")


# with example
with timer():
    '''measure the execution time'''
    time.sleep(2)

# multithreadind and multiprocessing
# techniques that can be used to improve performance of a python program

# multithreading is a technique where multiple threads are created within a single processing
# multirocessing is a technique where multiple threads are created

# example of multhreading


def task(name):
    print(f"running task {name}")


# create multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=task, args=(f"thread{i}",))
    threads.append(t)
    t.start

for t in threads:
    t.join()

# demonstrate multiprocessing


def process_task(name):
    print(f"processing task {name}")


# create a pool of process
pool = multiprocessing.pool(processes=5)

# submit multiple task to the pool
for i in range(6):
    pool.apply_async(process_task, args=(f"process.{i}",))

# close the pool and wait for all processto finish
pool.close()
pool.join()

# demonstrating multithreading and multiprocessing


def task(name):
    print(
        f"running task{name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")


# create multiple threads
threads = []
for i in range(4):
    t = threading.Thread(target=task, args=(f"thread{i}",))
    threads.append(t)
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()
