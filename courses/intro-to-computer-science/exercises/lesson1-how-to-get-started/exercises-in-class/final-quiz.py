# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

# find link
start_link = page.find('<a href=')
link = page[start_link:]

#find href
start_href = link.find('href="')
href = link[start_href:]

#find url
start_url = href.find('"') + 1
url = href[start_url:]

# Removing ">
url = url[:-2]