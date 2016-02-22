# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

print "f(0) =>", fibonacci(0)
# >>> 0
print "f(1) =>", fibonacci(1)
# >>> 1
print "f(2) =>", fibonacci(2)
# >>> 1
print "f(3) =>", fibonacci(3)
# >>> 2
print "f(4) =>", fibonacci(4)
# >>> 3
print "f(5) =>", fibonacci(5)
# >>> 5
print "f(6) =>", fibonacci(6)
# >>> 8
print "f(7) =>", fibonacci(7)
# >>> 13