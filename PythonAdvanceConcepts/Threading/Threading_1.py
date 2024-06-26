'''
Threading
allows you to execute multiple threads concurrently within a single process.
Threads share the same memory space, making it efficient for tasks that involve I/O-bound operations or tasks that don't require much CPU processing.
Python's threading module provides a high-level interface for working with threads.
'''
print("---------------------------------------------------------------------------------------------------------------")
# Creating Threads
# You can create threads by subclassing the Thread class and overriding the run() method.
import threading


class MyThread(threading.Thread):
    def run(self):
        print("Thread started")


# Create and start a thread
thread = MyThread()
thread.start()

print("\nAlternatively, you can pass a target function to the Thread constructor.")
# Alternatively, you can pass a target function to the Thread constructor.
import threading


def my_function():
    print("Thread started")


# Create and start a thread
thread = threading.Thread(target=my_function)
thread.start()

print(
    "\n---------------------------------------------------------------------------------------------------------------")
'''
Thread Synchronization

Threads can access shared resources concurrently, which can lead to race conditions and other synchronization issues. 
Python provides various synchronization primitives, such as locks, events, conditions, and 
semaphores, to coordinate access to shared resources among threads.
'''
import threading

shared_resource = 0
lock = threading.Lock()


def update_shared_resource():
    global shared_resource
    with lock:
        shared_resource += 1
        print(f"Updated shared resource: {shared_resource}")


# Create multiple threads to update shared resource
threads = []
for _ in range(5):
    thread = threading.Thread(target=update_shared_resource)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("---------------------------------------------------------------------------------------------------------------")
# Thread Communication
# Threads can communicate with each other using various mechanisms such as queues or event objects.

import threading
import queue


def producer(q):
    for i in range(5):
        q.put(i)


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Received item: {item}")


q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))
producer_thread.start()
consumer_thread.start()
producer_thread.join()
q.put(None)
consumer_thread.join()

print("---------------------------------------------------------------------------------------------------------------")
# Daemon Threads
# Daemon threads are threads that run in the background and automatically exit when the main program exits.
import threading
import time


def daemon_function():
    while True:
        print("Daemon thread is running")
        time.sleep(1)


daemon_thread = threading.Thread(target=daemon_function)
daemon_thread.daemon = True  # Set as daemon thread
daemon_thread.start()

time.sleep(5)  # Main thread sleeps for 5 seconds
print("Main thread exiting")

print("---------------------------------------------------------------------------------------------------------------")
import threading


def print_cube(num):
    print("Cube: {}".format(num * num * num))


def print_square(num):
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")

print("---------------------------------------------------------------------------------------------------------------")
import threading
import os


def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":
    print("ID of process running main program: {}".format(os.getpid()))

    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")
