# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

# Convert seconds in hours, minutes, seconds
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

	if hours > 1 or hours >= 0 and hours < 1:
		hours = str(hours) + " hours, "
	else:
		hours = str(hours) + " hour, "

	if minutes > 1 or minutes >= 0 and minutes < 1:
		minutes = str(minutes) + " minutes, "
	else:
		minutes = str(minutes) + " minute, "

	if seconds > 1 or seconds >= 0 and seconds < 1:
		seconds = str(seconds) + " seconds "
	else:
		seconds = str(seconds) + " second "

	string = hours + minutes + seconds
	return string 

def download_time(file_size, file_size_unity, download_size, download_size_unity):
	try:
		import math
	except:
		print "Error import math lib"
	
	# Sizes in Bits
	sizes = [["kb", math.pow(2,10)], 	 # 1024
			 ["kB", math.pow(2,10) * 8], # 8192.0
			 ["Mb", math.pow(2,20)], 	 # 1048576.0
			 ["MB", math.pow(2,20) * 8], # 8388608.0
			 ["Gb", math.pow(2,30)],	 # 1073741824.0
			 ["GB", math.pow(2,30) * 8], # 8589934592.0
			 ["Tb", math.pow(2,40)],	 # 1099511627776.0
			 ["TB", math.pow(2,40) * 8]] # 8796093022208.0

	# File size in Bits
	for size in sizes:
		if size[0] == file_size_unity:
			file_size *= size[1]

	# Download size in Bits
	for size in sizes:
		if size[0] == download_size_unity:
			download_size *= size[1]

	seconds = file_size / download_size
	return convert_seconds(seconds)

print download_time(1,'kB',3,'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


