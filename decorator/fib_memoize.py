class memoize(object):
	def __init__(self, f):
		print "initiating class memoize..."
		self.f = f
		self.fibArr = [-1 for _ in range(100)]
		print "initialized fibArr " + str(self.fibArr)

	def __call__(self, n):
		if self.fibArr[n] != -1 :
			return self.fibArr[n]
		self.fibArr[n] = self.f(n)
		print "fibArr[" + str(n) + "] = " + str(self.fibArr[n])
		return self.fibArr[n]

@memoize
def fib(n):
	"""Recursively computes nth fibonacci number"""
	return n if n in (0,1) else fib(n-1) + fib(n-2)

print fib(0)
print fib(1)
print fib(2)
print fib(3)
print fib(5)
print fib(10)
print fib(20)

