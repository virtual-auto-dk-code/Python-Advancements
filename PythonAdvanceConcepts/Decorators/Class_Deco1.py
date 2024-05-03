'''
Decorators can also be used with class
such as with class methods and even whole classes.
These type of decorators are referred to as "class-level decorators."
'''

print(
    "- Class Method Decorators --------------------------------------------------------------------------------------")
class MyClass:
    @classmethod
    def my_class_method(cls):
        print("This is a class method.")

    @classmethod
    def fun(cls):
        print("Fun class using class method decorator ...")

obj = MyClass()
MyClass.my_class_method()
MyClass.fun()


# obj = MyClass()
# obj.fun()

print("- Class Decorators --------------------------------------------------------------------------------------")


def get_custom_attribute(cls):
    cls.custom_attribute = "Added via class decorator"
    return cls


@get_custom_attribute
class MyClass:
    myclass_var = "This is class variable"

    def fun(self):
        print(MyClass.myclass_var)


print(MyClass.custom_attribute)
obj = MyClass()
obj.fun()

print("- Metaclass --------------------------------------------------------------------------------------")
