'''
The reduce() function in Python is used to apply a function iteratively to the items of an iterable, from left to right, to reduce the iterable to a single value.
It's part of the functools module in Python 3,
whereas in Python 2 it was available as a built-in function in the functools module.

functools.reduce(function, iterable[, initializer])

'''

print("---------------------------------------------------------------------------------------------------------------")

from functools import reduce

# Define a function to sum two numbers
def add(x, y):
    return x + y

# Apply reduce() to sum up a list of numbers
numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)
print("Sum of numbers:", result)


print("---------------------------------------------------------------------------------------------------------------")

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)

print("---------------------------------------------------------------------------------------------------------------")

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product_of_numbers)


print("---------------------------------------------------------------------------------------------------------------")

from functools import reduce

strings = ["Hello", ", ", "World", "!"]
concatenated_string = reduce(lambda x, y: x + y, strings)
print("Concatenated string:", concatenated_string)


print("---------------------------------------------------------------------------------------------------------------")

from functools import reduce

numbers = [10, 20, 5, 15, 30]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum value:", max_value)


print("---------------------------------------------------------------------------------------------------------------")

from functools import reduce

n = 5
factorial = reduce(lambda x, y: x * y, range(1, n+1))
print("Factorial of", n, "is:", factorial)


print("---------------------------------------------------------------------------------------------------------------")



print("---------------------------------------------------------------------------------------------------------------")



print("---------------------------------------------------------------------------------------------------------------")



print("---------------------------------------------------------------------------------------------------------------")