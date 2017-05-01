import urllib
import ast

# class Movie():
#
#     def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
#         self.title = movie_title
#         self.poster_image_url = poster_image_url
#         self.trailer_youtube_url = trailer_youtube_url


# Going to and get movie information from omdb api
class Movie():

    def __init__(self, movie_query, trailer_youtube_url):
        omdb_query_string = movie_query.replace(" ", "+")
        website = "http://www.omdbapi.com/?t="+omdb_query_string
        print(website)
        proxy = "http://10.32.1.8:10149"
        connection = urllib.urlopen(website, proxies = {'http': proxy})
        output = connection.read()
        print(output)
        dict_output = ast.literal_eval(output)
        self.title = dict_output["Title"]
        self.poster_image_url = dict_output["Poster"]
        self.trailer_youtube_url = trailer_youtube_url
