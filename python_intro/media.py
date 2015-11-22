import webbrowser
# Create a Movie class
class Movie():
    # Add __doc__ documentation for the class between """ """
    """This class provides a way to store information related to movies"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
# Create an init function that accepts variables when called
    def __init__(self, title, storyline, poster_url, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer
# Create a function to play the trailer when called
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
