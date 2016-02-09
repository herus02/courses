# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(string, char_list):
	words = []
	aux = True
	for char in string:
		if char not in char_list:
			if aux:
				words.append(char)
				aux = False
			else:
				words[-1] += char
		else:
			aux = True
	return words

passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")

char_list = [" "]
# char_list = [" ", ".", ",", "*"]

print count_words(passage, char_list)
#>>>56