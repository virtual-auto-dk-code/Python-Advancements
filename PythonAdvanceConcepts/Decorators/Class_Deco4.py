class PowerMe(object):
    def __init__(self, arg):
        print("I am in init")
        self._arg = arg
        print(arg)

    def __call__(self, *param_arg):
        """In case of arguments decorator __call__() is only called once
        for the decoration process. only a single argumentcan be given which is the function object.
        If there are no decorator arguments then the function to be decorated is passed to the constructor.
        """
        print("I am in call")
        print(str(len(param_arg)))
        print(str(param_arg))
        if len(param_arg) == 1:
            def wrapper(a, b):
                print(str(a) + " --- " + str(b))
                retval = param_arg[0](a, b)
                print(str(retval))
                return retval ** self._arg
            return wrapper
        else:
            expo = 2
            retval = self._arg(param_arg[0], param_arg[1])
            print(str(retval))
            return retval ** expo

@PowerMe
def multiply_all(a, b):
    print("I am in multiply")
    print(str(a) + " --- " + str(b))
    return a * b


print(multiply_all(2,3))

print("---------------------------------------------------------------------------------------------------------------")