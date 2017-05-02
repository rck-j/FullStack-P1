import media
import fresh_tomatoes

# Create Movie objects
pulp_fiction = media.Movie("Pulp Fiction",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

lost_translation = media.Movie("Lost in Translation",
                               "https://www.youtube.com/watch?v=sU0oZsqeG_s")

wall_e = media.Movie("WALL-E",
                     "https://www.youtube.com/watch?v=ZisWjdjs-gM")

matrix = media.Movie("The Matrix",
                     "https://www.youtube.com/watch?v=Q8g9zL-JL8E")

arrival = media.Movie("Arrival",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

o_brother = media.Movie("O Brother, Where Art Thou?",
                        "https://www.youtube.com/watch?v=eW9Xo2HtlJI")

# Create list of movies to be passed to fresh_tomatoes function open_movies_page
movies = [pulp_fiction, lost_translation, wall_e, matrix, arrival, o_brother]
fresh_tomatoes.open_movies_page(movies)
