'''
While the map() function applies a specified function to each element in an iterable and
returns the result of all elements having undergone the function, filter() operates differently.
It mandates that the provided function must return boolean values (true or false).
It then evaluates each element in the iterable against this function, essentially 'filtering' out those that return false.

The syntax for filter() is as follows:
filter(func, iterable)

Several key points distinguish filter() from map():
- Only one iterable is required, as opposed to map() which can accept multiple iterables.
- The func argument must return a boolean type; otherwise, filter() will simply return the original iterable.
  Given that only one iterable is accepted, it's implied that func should take only one argument.
- filter() processes each element in the iterable through func, returning only those elements that evaluate to true.
  This behavior is reflected in its name — it functions as a 'filter'.
'''

print("---------------------------------------------------------------------------------------------------------------")
print("With Filter")
marks = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def is_A_student(score):
    return score > 75


over_75 = list(filter(is_A_student, marks))
print(over_75)

print("---------------------------------------------------------------------------------------------------------------")

print("Without Filter")
marks = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def is_A_student(score):
    return score > 75


over_75 = list(filter(is_A_student, marks))
print(over_75)

print("---------------------------------------------------------------------------------------------------------------")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

print("---------------------------------------------------------------------------------------------------------------")
numbers = [-1, -2, 3, 4, -5, 6, 7, -8, 9, 10]

positive_numbers = list(filter(lambda x: x > 0, numbers))
print("Positive numbers:", positive_numbers)

print("---------------------------------------------------------------------------------------------------------------")
strings = ["apple", "banana", "orange", "kiwi", "grape"]

long_strings = list(filter(lambda x: len(x) > 5, strings))
print("Strings with length greater than 5:", long_strings)

print("---------------------------------------------------------------------------------------------------------------")
students = [
    {"name": "AAA", "age": 25},
    {"name": "BBB", "age": 30},
    {"name": "CCC", "age": 20},
    {"name": "DDD", "age": 35},
]

adult_students = list(filter(lambda x: x["age"] >= 18, students))
print("Adult students:", adult_students)

print("---------------------------------------------------------------------------------------------------------------")
values = [10, None, 20, None, 30, None, 40]

filtered_values = list(filter(None, values))
print("Filtered values:", filtered_values)

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")
