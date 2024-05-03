import functools
print("---------------------------------------------------------------------------------------------------------------")
def log_with_params(log_message):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling function: {func.__name__}")
            print(f"Log message: {log_message}")
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


# Usage example
@log_with_params("Fun Execution started")
def my_function():
    print("Inside my_function")


# Call the decorated function
my_function()

print("---------------------------------------------------------------------------------------------------------------")

# -----------------------------------------------------------------------------------------------------------------------
import functools

def validate_return_type(expected_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, expected_type):
                raise TypeError(f"Function {func.__name__} did not return expected type {expected_type.__name__}")
            return result
        return wrapper
    return decorator

# Usage example
@validate_return_type(int)
def add_numbers(a, b):
    return a + b

# Call the decorated function
result = add_numbers(22, 333)
print("Result of adding numbers:", result)

# This will raise an error since the return type is not int
result = add_numbers(7.5, 5.3)
# TypeError: Function add_numbers did not return expected type int

print("---------------------------------------------------------------------------------------------------------------")