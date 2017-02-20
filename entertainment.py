import media 
import fresh_tomatoes # render a list of movie images in html via a broswer

toy_story = media.Movie("Toy Story", "A story about a boy and his toys", 
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

gravity = media.Movie("Gravity", "Two astronauts in outer space", 
						"https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
						"https://www.youtube.com/watch?v=OiTiKOy59o4")

john_wick_2 = media.Movie("John Wick: Chapter 2", "A bounty on his life",
						"https://upload.wikimedia.org/wikipedia/en/3/31/John_Wick_Chapter_Two.png",
						"https://www.youtube.com/watch?v=XGk2EfbD_Ps")

rogue_one = media.Movie("Rogue One", "The Rebel Alliance makes a risky move to steal the plans for the Death Star", 
						"https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One,_A_Star_Wars_Story_poster.png",
						"https://www.youtube.com/watch?v=frdj1zb9sMY")

lord_of_the_rings = media.Movie("The Lord of the Rings: The Return of the King", "The final chapter", 
						"https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
						"https://www.youtube.com/watch?v=r5X-hFf6Bwo")

lala_land = media.Movie("La La Land", "Lame movie about a jazz pianist falling for an aspiring actress in Los Angeles.", 
						"https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_(film).png",
						"https://www.youtube.com/watch?v=0pdqf4P9MB8")

movies = [toy_story, gravity, john_wick_2, rogue_one, lord_of_the_rings, lala_land]
fresh_tomatoes.open_movies_page(movies)