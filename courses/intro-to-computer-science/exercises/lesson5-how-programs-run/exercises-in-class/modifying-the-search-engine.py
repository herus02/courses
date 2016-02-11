def add_to_index(index, keyword, url):
    if keyword in index:
    	if url in index[keyword]:
    		index[keyword].append(url)
    		return
    index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
    	return index[keyword]
    return None

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

# Get content page
def get_page(url):
  try:
    import urllib
    return urllib.urlopen(url).read()
  except:
    return ''

# Get next link
def get_next_target(page) :
	start_link = page.find('<a href=')
	if start_link == -1 :
		return None, 0
	else:
		start_quote = page.find('"', start_link)
		end_quote = page.find('"', start_quote + 1)
		url = page[start_quote + 1: end_quote]
		return url, end_quote

# Get and print all links from the page
def get_all_links(page):
	url_list = []
	while True:
		url, end_pos = get_next_target(page)
		if url:
			url_list.append(url)
			page = page[end_pos:]
		else:
			break
	return url_list

# Page content

def web_crawler(see):
	tocrawl = [see]
	crawled = []
	index = {}
	while tocrawl:
		print "Get Content Page: " + tocrawl[0]
		page = get_page(tocrawl[0])
		print "Adding page to index..."
		add_page_to_index(index, tocrawl[0], page)
		print "Procurando Links..." 
		links = get_all_links(page)
		print ""
		for current in links:
			if current not in crawled:
				tocrawl.append(current)
		crawled.append(tocrawl.pop(0))
	return index

index = web_crawler('https://www.udacity.com/cs101x/index.html')
print lookup(index, 'test')
print lookup(index, 'but')