'''
Iterators are objects that allow you to traverse through a sequence of elements.
They implement the iterator protocol,
which consists of two methods: __iter__() and __next__().
The __iter__() method returns the iterator object itself, and
the __next__() method returns the next element in the sequence.
When there are no more elements to return, it raises the StopIteration exception.

Iterators are objects in Python that represent a stream of data and can be iterated over using a loop (e.g., for loop).
They are implemented with two methods: __iter__() and __next__().

list, dicts like types are iterables
uses method __iter__()

generators use __next__()

and iterators use two methods: __iter__() and __next__()
'''
print("---------------------------------------------------------------------------------------------------------------")

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        current_element = self.data[self.index]
        self.index += 1
        return current_element


# Creating an instance of MyIterator
my_iterator = MyIterator([1, 2, 3, 4, 5])

# Iterating through the elements using a for loop
for element in my_iterator:
    print(element)

print("---------------------------------------------------------------------------------------------------------------")


#  Custom Iterator
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


my_iter = MyIterator([10, 20, 30, 40, 50])
for val in my_iter:
    print(val)

print("---------------------------------------------------------------------------------------------------------------")
# Built-in Iterators#
# Python provides built-in iterators for many objects, including lists, dictionaries, strings, etc.

# List iterator
my_list = [1, 2, 3, 4, 5]
list_iter = iter(my_list)
print(next(list_iter))  # Output: 1
print(next(list_iter))  # Output: 2

# String iterator
my_string = "Hello"
str_iter = iter(my_string)
print(next(str_iter))  # Output: 'H'
print(next(str_iter))  # Output: 'e'

print("---------------------------------------------------------------------------------------------------------------")
# Using Iterators with iter() and next()
my_iterable = iter([1, 2, 3])
print(next(my_iterable))  # Output: 1
print(next(my_iterable))  # Output: 2
print(next(my_iterable))  # Output: 3
# print(next(my_iterable))  # Uncommenting this will raise StopIteration error

print("---------------------------------------------------------------------------------------------------------------")


# Infinite Iterator
class InfiniteIterator:
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        self.num += 1
        return self.num


infinite_iter = InfiniteIterator()
for i in infinite_iter:
    if i > 20:
        break
    print(i)

print("---------------------------------------------------------------------------------------------------------------")


# Filtering Iterator
# You can create an iterator that filters elements based on a certain condition.
class FilterIterator:
    def __init__(self, iterable, condition):
        self.iterable = iterable
        self.condition = condition

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            element = next(self.iterable)
            if self.condition(element):
                return element


# Example usage:
numbers = iter(range(10))
filtered_numbers = FilterIterator(numbers, lambda x: x % 2 == 0)
for num in filtered_numbers:
    print(num)

print("---------------------------------------------------------------------------------------------------------------")


# Zip Iterator
# You can create an iterator that combines elements from multiple iterables.

class ZipIterator:
    def __init__(self, *iterables):
        print(*iterables)
        self.iterables = iterables
        print(iterables)

    def __iter__(self):
        return self

    def __next__(self):
        print(self.iterables)
        result = tuple(next(it) for it in self.iterables)
        if result:
            print(result)
            return result
        else:
            raise StopIteration


# Example usage:
numbers = iter(range(1, 6))
# print(numbers)
# try:
#     while True:
#         print(next(numbers))
# except StopIteration:
#     pass

letters = iter(['a', 'b', 'c', 'd', 'e'])
# print(letters)
# try:
#     while True:
#         print(next(letters))
# except StopIteration:
#     pass

zipped = ZipIterator(numbers, letters)

# print(zipped)
# try:
#     while True:
#         print(next(zipped))
# except StopIteration:
#     pass

for item in zipped:
    print(item)

print("---------------------------------------------------------------------------------------------------------------")
#  Run independently -----
# Cycle Iterator
# You can create an iterator that cycles endlessly through a sequence
class CycleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)


# Example usage:
colors = CycleIterator(['red', 'green', 'blue'])
for _ in range(10):
    print(next(colors))

print("---------------------------------------------------------------------------------------------------------------")

# Run independently
# Define an iterator class
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


# Create an instance of the iterator
my_iter = MyIterator([10, 20, 30, 40, 50])

# Using a for loop to print values
print("Printing values using a for loop:")
for val in my_iter:
    print(val)

# Reinitialize the iterator
my_iter = MyIterator([10, 20, 30, 40, 50])

# Using next() function to print values
print("\nPrinting values using next() function:")
try:
    while True:
        print(next(my_iter))
except StopIteration:
    pass

print("---------------------------------------------------------------------------------------------------------------")
