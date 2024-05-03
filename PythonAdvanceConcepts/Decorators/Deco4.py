from time import time

def timer(func):
    def wrapper(*args,**kwargs):
        before = time()
        rv = func(*args,**kwargs)
        after = time()
        tot_time = after - before
        print("Time Taken : "+str(tot_time))
        return rv
    return wrapper
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add = timer(add)
print(add)
print(add(10,20))


print("--------------------------------------------------")

def timer(func):
    def wrapper(*args,**kwargs):
        before = time()
        rv = func(*args,**kwargs)
        after = time()
        tot_time = after - before
        print("Time Taken : "+str(tot_time))
        return rv
    return wrapper

@timer
def add(x,y):
    return x+y

@timer
def sub(x,y):
    return x-y


print(add(10,20))