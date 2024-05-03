class GetPower(object):
	def __init__(self, arg):
		self._arg = arg

	def __call__(self, x, y):
		retval = self._arg(x, y)
		return retval ** 2


@GetPower
def multiply(x, y):
	return x * y


print(multiply)
print(multiply(2, 2))