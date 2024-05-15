'''
A powerful tool for creating iterators.
They allow you to iterate over a set of items without the need to store them all in memory at once,
which is particularly useful when dealing with large datasets.

Generator Functions: These are functions that contain one or more yield statements.
When called, a generator function returns a generator object,
which can then be iterated over using a for loop or by calling the next() function on it.

Generator Expressions:
These are similar to list comprehensions but use round parentheses () instead of square brackets [].
They generate values on the fly rather than constructing a list.

Generators are memory efficient because they only produce one item at a time and maintain their state between calls.
This makes them ideal for tasks such as iterating over large files or databases, generating infinite sequences, and processing data streams in real-time.
'''

print("---------------------------------------------------------------------------------------------------------------")
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

print("---------------------------------------------------------------------------------------------------------------")
gen = (x for x in range(3))
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

print("---------------------------------------------------------------------------------------------------------------")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(15):
    print("--- Current loop Iteration "+str(_)+"---")
    print(next(fib))  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

print("---------------------------------------------------------------------------------------------------------------")

numbers = [10, 20, 33, 40, 55, 60, 77, 80, 99, 100]
even_gen = (x for x in numbers if x % 2 == 0)
for num in even_gen:
    print(num)  # Output: 20, 40, 60, 80, 100

print("---------------------------------------------------------------------------------------------------------------")



print("---------------------------------------------------------------------------------------------------------------")



print("---------------------------------------------------------------------------------------------------------------")



print("---------------------------------------------------------------------------------------------------------------")



print("---------------------------------------------------------------------------------------------------------------")



print("---------------------------------------------------------------------------------------------------------------")