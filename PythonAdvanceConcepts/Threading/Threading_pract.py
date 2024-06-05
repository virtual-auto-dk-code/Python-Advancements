import threading
import time
import random


def print_names():
    for name in ("AA", "BB", "CC"):
        print(name)
        time.sleep(random.uniform(0.5, 1.5))
        # time.sleep(2)


def print_age(min_sleep, max_sleep):
    for _ in range(5):
        print(random.randint(min_sleep, max_sleep))
        time.sleep(0.5)


t1 = threading.Thread(target=print_names)
min_sleep = 20
max_sleep = 50
t2 = threading.Thread(target=print_age, args=(min_sleep, max_sleep,))

t1.start() # Init Thread
t2.start()

t1.join() # Terminate Thread
t2.join()

print("---------------------------------------------------------------------------------------------------------------")
