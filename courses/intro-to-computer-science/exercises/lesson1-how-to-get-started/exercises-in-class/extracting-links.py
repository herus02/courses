# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

# find <a href="...">...</a>
start_link = page.find('<a href="')
page = page[start_link:]

# find href="..."
start_href = page.find('href="')
page = page[start_href:]

# get url
start_url = page.find('"') + 1
page = page[start_url:]

# removing ">
page = page[:-2]
