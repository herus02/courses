# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
	# Number minimum for buckets
	if buckets < 1:
		return 0

	# Checking empty string
	if not keyword:
		return 0

	# Compute the sum of the numbers
	sum_chrs = 0
	for char in keyword:
		sum_chrs += ord(char)
	
	# return bucket
	return sum_chrs % buckets

def test_hash_function(func, key, size):
	results = [0] * size
	key_used = []
	for w in key:
		if w now in key_used:
			hv = func(w, size)
			results[hv] += 1
			key_used.append(w)
	return results

print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11