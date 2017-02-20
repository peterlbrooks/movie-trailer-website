import webbrowser

class Movie():

	"""The Movie class defines movie attributes and provides a function to show the trailer

	Arttributes:     

	movie_title: text title of the movie     
	moview_storyline: short generally 80 chars or less description of the movie
	poster_image: thumbnail html-presentable image of the movie
	trailer_youtube: movie trailer from youtube
	"""
	
	def __init__(self, movie_title, movie_storyline, poster_image, 
				trailer_youtube) :

        #Initializes movie atributes
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
	def show_trailer(self) :

		# Shows the movie trailer in a web browser
		webbrowser.open(self.trailer_youtube_url)
		
