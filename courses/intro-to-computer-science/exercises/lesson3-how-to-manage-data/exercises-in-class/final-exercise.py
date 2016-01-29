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
	while tocrawl:
		print "Get Content Page: " + tocrawl[0]
		page = get_page(tocrawl[0])
		print "Procurando Links..." 
		links = get_all_links(page)
		print ""
		for current in links:
			if current not in crawled:
				tocrawl.append(current)
		crawled.append(tocrawl.pop(0))
	return crawled

def print_all_links():
	links = web_crawler('https://www.udacity.com/cs101x/index.html')
	for current in links:
		print current
		print ""
	return

print_all_links()