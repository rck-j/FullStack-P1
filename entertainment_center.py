import media
import fresh_tomatoes

#Create Movie objects
# pulp_fiction = media.Movie("Pulp Fiction",
#                            "https://upload.wikimedia.org/wikipedia/" \
#                            "en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
#                            "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
#
# lost_translation = media.Movie("Lost in Translation",
#                                "https://upload.wikimedia.org/wikipedia/" \
#                                "en/4/4c/Lost_in_Translation_poster.jpg",
#                                "https://www.youtube.com/watch?v=sU0oZsqeG_s")
#
# wall_e = media.Movie("WALL-E",
#                      "https://upload.wikimedia.org/wikipedia" \
#                      "/en/c/c2/WALL-Eposter.jpg",
#                      "https://www.youtube.com/watch?v=ZisWjdjs-gM")
#
# matrix = media.Movie("The Matrix",
#                      "https://upload.wikimedia.org/wikipedia/" \
#                      "en/c/c1/The_Matrix_Poster.jpg",
#                      "https://www.youtube.com/watch?v=Q8g9zL-JL8E")
#
# arrival = media.Movie("Arrival",
#                       "https://upload.wikimedia.org/wikipedia/" \
#                       "en/d/df/Arrival%2C_Movie_Poster.jpg",
#                       "https://www.youtube.com/watch?v=tFMo3UJ4B4g")
#
# o_brother = media.Movie("O Brother, Where Art Thou?",
#                         "https://upload.wikimedia.org/wikipedia/" \
#                         "en/5/5b/O_brother_where_art_thou_ver1.jpg",
#                         "https://www.youtube.com/watch?v=eW9Xo2HtlJI")

#Crete list of movies to be passed to fresh_tomatoes function open_movies_page
#movies = [pulp_fiction, lost_translation, wall_e, matrix, arrival, o_brother]
pulp_fiction = media.Movie("the matrix", "https://www.youtube.com/watch?v=Q8g9zL-JL8E")
movies = [pulp_fiction]
fresh_tomatoes.open_movies_page(movies)
