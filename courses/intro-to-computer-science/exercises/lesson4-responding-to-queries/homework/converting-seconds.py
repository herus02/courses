# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(numbers):
	hours, minutes, seconds, i = 0, 0 ,0, 0
	string = ""

	while i < numbers:
		if i == 60:
			minutes += 1
			numbers -= 60
			i = 0
		if minutes == 60:
			hours += 1
			minutes = 0
			i = 0
		i += 1

	seconds += numbers
	if seconds == 60:
		minutes += 1
		seconds = 0
		if minutes == 60:
			hours += 1
			minutes = 0

	print "number =>", numbers

	if hours > 1 or hours == 0:
		hours = str(hours) + " hours, "
	else:
		hours = str(hours) + " hour, "

	if minutes > 1 or minutes == 0:
		minutes = str(minutes) + " minutes, "
	else:
		minutes = str(minutes) + " minute, "

	if seconds > 1 or seconds == 0:
		seconds = str(seconds) + " seconds "
	else:
		seconds = str(seconds) + " second "

	string = hours + minutes + seconds
	return string 

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

print convert_seconds(2377.14285714)