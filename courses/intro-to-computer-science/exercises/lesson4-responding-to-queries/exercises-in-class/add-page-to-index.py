# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []

def word_is_in_index(word, index):
	for current in index:
		if current[0] == word:
			return current
	return []

def insert_url(word, url, list_index):
	if list_index:
		for current_url in list_index[1]:
			if current_url == url:
				return []
		list_index[1].append(url)
		return []
	else:
		list_index.append(word)
		list_index.append([url])
		return list_index

def add_page_to_index(index,url,content):
	content = content.split()
	for word in content:
		result = insert_url(word, url, word_is_in_index(word, index))
		if result:
			index.append(result)

add_page_to_index(index, 'fake.text', 'This is a test')
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]