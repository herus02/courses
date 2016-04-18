import webbrowser

class Movie(object):
  """Movie Class Documentation for print with __doc__"""

  # class varible example
  VALID_RATINGS = ["G", "PG", "PG-13", "R"]

  def __init__(felipe, movie_title, movie_storyline, image_poster_url, trailer_youtube_url ):
    felipe.title = movie_title
    felipe.storyline = movie_storyline
    felipe.poster_image_url = image_poster_url
    felipe.trailer_youtube_url = trailer_youtube_url

  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
