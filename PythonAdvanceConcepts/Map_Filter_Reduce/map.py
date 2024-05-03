'''
syntax:
map(func, *iterables)

In Python 2, the map() function returns a list.
However, in Python 3, the function returns a map object, which is an iterable generator object.
To obtain the result as a list in Python 3, you can use the built-in list() function, passing the map object as an argument.
For example, list(map(func, *iterables)) will return the mapped values as a list.

The function func must be provided with the same number of arguments as the number of iterables listed.
'''

print("---------------------------------------------------------------------------------------------------------------")
print("Simple Program without MAP")
my_items = ['aa', 'bb', 'cc', 'dd']
uppered_items = []

for item in my_items:
    item_ = item.upper()
    uppered_items.append(item_)

print(uppered_items)
print("---------------------------------------------------------------------------------------------------------------")

print("Program with MAP")
my_items = ['aa', 'bb', 'cc', 'dd']
uppered_items = list(map(str.upper, my_items))
# Note : Not implicit call to the str.upper function (using this: str.upper()), as the map function does that on each element in the my_items list.
print(uppered_items)

print("---------------------------------------------------------------------------------------------------------------")

my_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, my_areas, range(1, 7)))

print(result)

'''
The range(1, 7) function acts as the second argument to the round function (the number of required decimal places per iteration). 
So as map iterates through my_areas, during the 
first iteration, the first element of my_areas, 3.56773 is passed along with the first element of range(1,7), 1 to round, 
making it effectively become round(3.56773, 1). 
During the second iteration, the second element of my_areas, 5.57668 along with the second element of range(1,7), 2 is passed to round 
making it translate to round(5.57668, 2). This happens until the end of the my_areas list is reached.
'''
print("---------------------------------------------------------------------------------------------------------------")

my_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, my_areas))
print(result)

print("---------------------------------------------------------------------------------------------------------------")
print(" Using Zip ")
my_str_lst = ['a', 'b', 'c', 'd', 'e']
my_number_lst = [1, 2, 3, 4, 5]
results = list(zip(my_str_lst, my_number_lst)) #own custom zip() function
print(results)

print("---------------------------------------------------------------------------------------------------------------")

print(" Using Map ")
my_str_lst = ['a', 'b', 'c', 'd', 'e']
my_number_lst = [1, 2, 3, 4, 5]
results = list(map(lambda x, y: (x, y), my_str_lst, my_number_lst))
print(results)

print("---------------------------------------------------------------------------------------------------------------")