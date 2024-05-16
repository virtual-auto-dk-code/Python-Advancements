'''
lambda:
A small anonymous function defined using the lambda keyword.
It can take any number of arguments but can only have one expression.
Often used as a concise way to create simple functions without the need to define a function using the def keyword.

Syntax:
lambda arguments: expression

'''
print("---------------------------------------------------------------------------------------------------------------")

test = lambda x:x*x
print(test(5))

def sq(x):
    return x*x

print(sq(5))

print("---------------------------------------------------------------------------------------------------------------")

num_ls = [1,2,3,4,5]
double_lst = list(map(lambda x: x*3,num_ls))
print(double_lst)

double_lst_compreh = [num*3 for num in num_ls]
print(double_lst_compreh)

print("---------------------------------------------------------------------------------------------------------------")
lst_emp =[
    {'name':'aaa','age':35},
    {'name':'bbb','age':30},
    {'name':'ccc','age':25},
    {'name':'ddd','age':37},
    {'name':'eee','age':40},
]

names = list(map(lambda x:x['name']+'_'+str(x['age']),lst_emp))
print(names)

print("---------------------------------------------------------------------------------------------------------------")

num_lst = [1,2,3,4,5]
even_nums = list(filter(lambda x: x % 2 != 0,num_lst))
print(even_nums)
even_nums = list(filter(lambda x: x % 2 == 0,num_lst))
print(even_nums)

print("---------------------------------------------------------------------------------------------------------------")

square = lambda x: x ** 2
print(square(5))  # Output: 25

print("---------------------------------------------------------------------------------------------------------------")

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

print("---------------------------------------------------------------------------------------------------------------")
