#  a Python Class Decorator

class PowerMe(object):
	def __init__(self, arg):
		print("I am in init")
		print(arg)
		self._arg = arg

	def __call__(self, a, b):
		print("I am in call")
		print(str(a)+" --- "+str(b))
		retval = self._arg(a, b)
		print(str(retval))
		return retval ** 2


@PowerMe
def multiply_all(a, b):
	print("I am in multiply")
	return a * b

print("---------------------------------------------------------------------------------------------------------------")
print(multiply_all)
print("---------------------------------------------------------------------------------------------------------------")
print(multiply_all(7, 4))
print("---------------------------------------------------------------------------------------------------------------")
