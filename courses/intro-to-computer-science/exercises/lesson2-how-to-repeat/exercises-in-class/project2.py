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

# Page content
page = get_page('http://xkcd.com/353')

# Get and print all links from the page
def print_all_links(page):
	while True:
		url, end_pos = get_next_target(page)
		if url:
			print url
			page = page[end_pos:]
		else:
			break

print_all_links(page)