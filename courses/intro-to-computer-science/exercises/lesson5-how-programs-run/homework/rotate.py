# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    letter_index = ord(letter) - ord('a') # one of 0, 1, 2, ..., 25
    shifted_index = (letter_index + n) % 26 # still one of 0, 1, 2, ..., 25
    return chr(ord('a') + shifted_index)

def rotate(string, n):
    new_string = ""
    for char in string:
    	if char != " ":
    		new_string += shift_n_letters(char, n)
    	else:
    		new_string += char
    return new_string

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???