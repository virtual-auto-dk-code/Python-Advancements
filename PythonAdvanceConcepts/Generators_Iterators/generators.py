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
This makes them ideal for tasks such as iterating over large files or databases, generating infinite sequences,
and processing data streams in real-time.

Generators in Python are typically created using the yield keyword to produce a series of values lazily,
allowing them to be iterated over efficiently.
However, it's also possible to create generators without using yield by using generator expressions.

Generator expressions are similar to list comprehensions but create generators instead of lists.
They have a syntax similar to list comprehensions but surrounded by parentheses instead of square brackets.
Generator expressions are evaluated lazily, meaning they produce values on-the-fly as they are iterated over,
which can save memory compared to creating a list.

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

# Generator without yield
even_numbers_generator = (x for x in range(11) if x % 2 == 0)
print(type(even_numbers_generator))

# Get output way 1
print("using next ...")
print(next(even_numbers_generator))
print(next(even_numbers_generator))

# Get output way 2
print("using for ...")
for num in even_numbers_generator:
    print(num)

'''
One thing to note is that unlike generator functions created using yield, 
generator expressions cannot be paused and resumed manually.
They are more limited in functionality compared to generator functions 
but can be quite handy for simple cases where lazily producing values is all that's required.
'''

print("---------------------------------------------------------------------------------------------------------------")
# Generators can encapsulate complex logic and state.
def countdown(start):
    while start > 0:
        yield start
        start -= 1
    yield 'Blast off!'

for val in countdown(5):
    print(val)

print("---------------------------------------------------------------------------------------------------------------")
# Generator Comprehension
# Generator expressions can be used to create generators concisely.
even_numbers_generator = (x for x in range(10) if x % 2 == 0)
for num in even_numbers_generator:
    print(num)

print("---------------------------------------------------------------------------------------------------------------")
# Generator for File Processing
# Generators can be used to process large files lazily, line by line, without loading the entire file into memory.
def process_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()

for line in process_file('example.txt'):
    print(line)



print("---------------------------------------------------------------------------------------------------------------")
# Generator Pipeline
# Generators can be chained together to form a pipeline for data processing.
def squares(nums):
    for num in nums:
        yield num ** 2

def even(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

nums = range(10)
pipeline = even(squares(nums))
for num in pipeline:
    print(num)


print("---------------------------------------------------------------------------------------------------------------")