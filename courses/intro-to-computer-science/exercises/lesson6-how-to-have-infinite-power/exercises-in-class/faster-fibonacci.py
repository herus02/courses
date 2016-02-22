# Define a faster fibonacci procedure that will enable us to computer
# fibonacci(36).

# fibonacci:
# 0 1 1 2 3 5 8 13 ...

def fibonacci(n):
	if n < 0:
		return -1

	n1, n2, count = 0, 1, 0
	while count < n:
		n1, n2 = n2, n1 + n2
		count += 1
	return n1

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
print "f(36) =>", fibonacci(36)
#>>> 14930352