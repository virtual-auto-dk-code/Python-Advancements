import os

list1 = ['a.1','b.2','c.3']
for items in list1:
    alpha,number = items.split('.')
    print(alpha,number)


# Command - export LIST_ITEMS = 'a.1', 'b.2', 'c.3'



os.environ["LIST_ITEMS"] = "a.1 b.2 c.3"

'''
list1 = [os.environ.get("LIST_ITEMS")]
for items in list1:
    alpha,number = items.split('.')
    print(alpha,number)
'''

list1 = [i.split(".") for i in os.environ.get("LIST_ITEMS").split(" ")]

for k, v in list1:
    print(k, v)