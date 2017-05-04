import urllib
import ast

class Movie():

    def __init__(self, movie_query, trailer_youtube_url):

        # Format string for querying omdb
        omdb_query_string = movie_query.replace(" ", "+")

        # Connect to omdbapi.com to get Title and Poster information
        website = "http://www.omdbapi.com/?t="+omdb_query_string
        connection = urllib.urlopen(website)
        output = connection.read()

        # Convert string return from omdb to a dictionary
        dict_output = ast.literal_eval(output)

        self.title = dict_output["Title"]
        self.poster_image_url = dict_output["Poster"]
        self.plot = dict_output["Plot"]
        self.trailer_youtube_url = trailer_youtube_url
