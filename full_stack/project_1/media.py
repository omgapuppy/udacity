import webbrowser
# Create a Movie class
class Movie():
# Create an init function that accepts variables when called
    def __init__(self, title, storyline, poster_url, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer
# Create a function to play the trailer when called
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
