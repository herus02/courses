# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

# Checking if the string is empty
def isEmpty(string):
	if string == "":
		return False
	return True

# Break the a string
def split_string(source,splitlist):
	words = []
	for char in source:
		for split in splitlist:
			if split == char:
				word = source[:source.find(char)]
				if isEmpty(word):
					words.append(word)
				source = source[source.find(char) + 1:]
				break
	if source:
		words.append(source)
	return words

#
# Solution Instructor
#
# def split_string(source, splitlist):
# 	output = []
# 	atsplit = True
# 	for char in source:
# 		if char in splitlist:
#			atsplit = False
#		else:
#			if atsplit:
#				output.append(char)
#				atsplit = False
#			else:
#				# add character to last word
#				output[-1] = output[-1] + char
#

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
print ""
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
print ""
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
print ""
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']