'''
Multiprocessing:
Python allows you to leverage multiple CPU cores to parallelize and speed up the execution of your programs.
Python provides the multiprocessing module, which makes it easy to create and manage multiple processes.

'''
print("---------------------------------------------------------------------------------------------------------------")
# Creating Processes
# You can create new processes using the Process class from the multiprocessing module.

import multiprocessing
import os


def worker():
    """Function to be executed by each process."""
    print(f"Worker process ID: {os.getpid()}")


if __name__ == "__main__":
    # Create multiple processes
    processes = []
    for _ in range(5):
        process = multiprocessing.Process(target=worker)
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

print("---------------------------------------------------------------------------------------------------------------")
# Passing Data Between Processes
# Processes can share data using shared memory, queues, or pipes provided by the multiprocessing module.
import multiprocessing


def worker(shared_value):
    """Function to be executed by each process."""
    shared_value.value += 1
    print(f"Updated value: {shared_value.value}")


if __name__ == "__main__":
    shared_value = multiprocessing.Value('i', 0)
    processes = []
    for _ in range(5):
        process = multiprocessing.Process(target=worker, args=(shared_value,))
        processes.append(process)
        print(processes)
        process.start()

    for process in processes:
        process.join()

print("--------------")
# Queues
import multiprocessing


def worker(queue):
    """Function to be executed by each process."""
    item = queue.get()
    print(f"Received item: {item}")


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    for i in range(5):
        queue.put(i)

    processes = []
    for _ in range(3):
        process = multiprocessing.Process(target=worker, args=(queue,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

print("---------------------------------------------------------------------------------------------------------------")
# Pooling Processes
# The Pool class from the multiprocessing module provides a convenient way to manage a pool of worker processes.

import multiprocessing


def worker(x):
    """Function to be executed by each process."""
    return x ** 2


if __name__ == "__main__":
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(worker, range(10))
        print(results)

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")
