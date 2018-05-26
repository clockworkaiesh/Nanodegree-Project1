import webbrowser


class Movie():

    """ 
        class "Movie()"stores all the details about a movie like it's title,
        story line, poster image and movie's trailer. Every time you will
        create a new instance of class "Movie()" in entertainment_center.py
        all of the info you provide there would be saved in class "Movie()"
        which is inside media.py.

        Class "Movie()" also has a function called
        "show_trailer()" which will open the trailer for the movie in browser
        when you click on that movie.

    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
