# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric(matrix):
	# Checking if the array is nxn
	if matrix == []:
		return True

	if len(matrix) != len(matrix[0]):
		return False
	
	i = 0
	n = len(matrix)
	
	# Calculating a list is symmetric
	while i < n:
		j = 0
		while j < n:
			if matrix[i][j] != matrix[j][i]:
				return False
			j += 1
		i += 1
	return True

print symmetric([[1, 2, 3],
				 [2, 3, 4],
				 [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
				 ["dog", "dog", "fish"],
				 ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
				 ["dog", "dog", "dog"],
				 ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
				 [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
				 [2, 3, 4, 5],
				 [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
				 [2,3,1]])
#>>> False