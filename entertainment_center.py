import media
import fresh_tomatoes

pulp_fiction = media.Movie("Pulp Fiction", "Stuff", "https://en.wikipedia.org/wiki/Pulp_Fiction#/media/File:Pulp_Fiction_(1994)_poster.jpg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
lost_translation = media.Movie("Lost in Translation", "Stuff", "https://en.wikipedia.org/wiki/Pulp_Fiction#/media/File:Pulp_Fiction_(1994)_poster.jpg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
wall_e = media.Movie("WALL-E", "Stuff", "https://en.wikipedia.org/wiki/Pulp_Fiction#/media/File:Pulp_Fiction_(1994)_poster.jpg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
matrix = media.Movie("The Matrix", "Stuff", "https://en.wikipedia.org/wiki/Pulp_Fiction#/media/File:Pulp_Fiction_(1994)_poster.jpg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
arrival = media.Movie("Arrival", "Stuff", "https://en.wikipedia.org/wiki/Pulp_Fiction#/media/File:Pulp_Fiction_(1994)_poster.jpg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
o_brother = media.Movie("O Brother, Where Art Thou?", "Stuff", "https://en.wikipedia.org/wiki/Pulp_Fiction#/media/File:Pulp_Fiction_(1994)_poster.jpg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

movies = [pulp_fiction, lost_translation, wall_e, matrix, arrival, o_brother]
fresh_tomatoes.open_movies_page(movies)
