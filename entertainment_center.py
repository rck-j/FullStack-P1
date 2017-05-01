import media
import fresh_tomatoes

pulp_fiction = media.Movie("Pulp Fiction", "Stuff", poster_image_url, trailer_youtube_url)
lost_translation = media.Movie("Lost in Translation", "Stuff", poster_image_url, trailer_youtube_url)
wall_e = media.Movie("WALL-E", "Stuff", poster_image_url, trailer_youtube_url)
matrix = media.Movie("The Matrix", "Stuff", poster_image_url, trailer_youtube_url)
arrival = media.Movie("Arrival", "Stuff", poster_image_url, trailer_youtube_url)
o_brother = media.Movie("O Brother, Where Art Thou?", "Stuff", poster_image_url, trailer_youtube_url)

movies = [pulp_fiction, lost_translation, wall_e, matrix, arrival, o_brother]
fresh_tomatoes.open_movies_page(movies)
