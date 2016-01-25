# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
  if n <= 1:
  	return 1
  else:
    fat = n
    while n > 1:
      fat = fat * (n - 1)  
      n = n - 1
    return fat
        


print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720

