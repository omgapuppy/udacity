import webbrowser

class Movie():
    def __init__(self, title, storyline, poster_url, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
