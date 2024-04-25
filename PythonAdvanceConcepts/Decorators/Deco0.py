'''
Decorators : Io modify or extend the behavior of functions or methods at the time of their definition.
Also allow to wrap another function or method and
execute code before and/or after the wrapped function runs.
Decorators are denoted by the '@' symbol followed by the decorator function name, placed on the line before the function definition.

Usage:
-   Without modifying original function definition
    allows logging of function calls, parameters, return values
-   Certain function level Authentication or Authorization
-
'''
def my_decorator(func):
    def wrapper():
        print("Before the function is called...")
        func()
        print("After the function is called...")
    return wrapper

@my_decorator
def say_hello_world():
    print("Hello World!")

say_hello_world()

print("- Logging ----------------------------------------------------------------------------")

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs) + kwargs["extra_para"]
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function
def add(*args,**kwargs):
    return args[0] + args[1]

result = add(3, 5, extra_para=9)


print("- Authentication ---------------------------------------------------------------------------------")


def is_user_authenticated():
    return True #False #


def authenticate(func):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            return func(*args, **kwargs)
        else:
            print("Unauthorized User!")
            raise PermissionError("User not authenticated")
    return wrapper

@authenticate
def sensitive_operation():
    # Do sensitive operation
    print("This is sensitive operation")


sensitive_operation()

print("- Cache ----------------------------------------------------------------------------")

def memorize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
            print(cache)
        return cache[args]

    return wrapper

@memorize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)  # This call will be cached

print(result)


print("- Cache ----------------------------------------------------------------------------")

import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

@timeit
def time_consuming_task():
    # Do time-consuming task
    print("Hello Its too time consuming!")


time_consuming_task()