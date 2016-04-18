import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
  'A story of a boy and his toys that come to life',
  'http://static.omelete.uol.com.br/media/extras/conteudos/toy_story_wallpaper_by_artifypics-d5gss19.jpg',
  'https://www.youtube.com/watch?v=msAciPMZdMM')

# class varible example
print "class varible =>", toy_story.VALID_RATINGS
print "predefined class varible =>", media.Movie.__doc__
print "predefined class varible =>", media.Movie.__name__

# movies = [toy_story]
# fresh_tomatoes.open_movies_page(movies)