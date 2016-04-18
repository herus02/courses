import urllib

def read_text():
  quotes = open('/home/felipe/Documents/github/courses/courses/programming-foundations-with-python/lesson2c-use-classes-profanity-editor/movie_quotes.txt')
  content = quotes.read()
  quotes.close()
  return content

def check_profanity(text):
  profanity_true = 'profanity alert!!'
  profanity_false = 'This document has no curse words!'
  connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
  output = connection.read()
  if 'true' in output:
    print profanity_true
  elif 'false' in output:
    print profanity_false
  else:
    print 'Could not scan the document properly'

  connection.close()

check_profanity(read_text())