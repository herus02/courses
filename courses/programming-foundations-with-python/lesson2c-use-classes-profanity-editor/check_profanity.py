def read_text():
  quotes = open('/home/felipe/Documents/github/courses/courses/programming-foundations-with-python/lesson2c-use-classes-profanity-editor/movie_quotes.txt')
  content = quotes.read()
  print content
  quotes.close()

read_text()