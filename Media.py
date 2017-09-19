# Create class movies that defines the type of information to hold for each movie  # NOQA


class Movie():
    """This class contains the definition function for storing the
    properties of each instance of class Movie"""
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """This constructor method takes the movie properties as
        arguments and assigns them to the class variables that
        store the information"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
