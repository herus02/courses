# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

#def median(a, b, c):
#	if a >= b and a <= c or a <= b and a >= c:
#    return a
#	else:
#    if b >= a and b <= c or b <= a and b >= c:
#      return b
#    else:
#      if c >= a and c <= b or c <= a and c >= b:
#        return c
#      else:
#        return a

def bigger(a,b):
  if a > b:
    return a
  else:
    return b

def biggest(a,b,c):
  return bigger(a,bigger(b,c))

def median(a, b, c):
	big = biggest(a, b, c)
	if big == a:
		return bigger(b,c)
	if big == b:
		return bigger(a,c)
	else:
		return bigger(a,b)
            
print median(4,3,3)
#>>> 2

print median(9,3,6)
#>>> 6

print median(7,8,7)
#>>> 7







