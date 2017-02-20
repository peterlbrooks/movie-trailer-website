import media
import fresh_tomatoes  # render a list of movie images in html via a browser

string = "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
toy_story = media.Movie("Toy Story", "A story about a boy and his toys",
                        string, "https://www.youtube.com/watch?v=KYz2wyBy3kc")

string = "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg"
gravity = media.Movie("Gravity", "Two astronauts in outer space",
                      string, "https://www.youtube.com/watch?v=OiTiKOy59o4")

string = "https://upload.wikimedia.org/wikipedia" + \
  "/en/3/31/John_Wick_Chapter_Two.png"
john_wick_2 = media.Movie("John Wick: Chapter 2", "A bounty on his life",
                          string,
                          "https://www.youtube.com/watch?v=XGk2EfbD_Ps")

string = "The Rebel Alliance makes a risky move to steal" + \
  " the plans for the Death Star"
string2 = "https://upload.wikimedia.org/wikipedia/" + \
  "en/d/d4/Rogue_One,_A_Star_Wars_Story_poster.png"

rogue_one = media.Movie("Rogue One", string, string2,
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

string = "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_" + \
  "the_Rings_-_The_Return_of_the_King.jpg"
lord_of_the_rings = media.Movie(
    "The Lord of the Rings: The Return of the King", "The final chapter",
    string, "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

string = "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_(film).png"
lala_land = media.Movie("La La Land",
                        "Lame movie about a jazz pianist and actress",
                        string,
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")

movies = [toy_story, gravity, john_wick_2,
          rogue_one, lord_of_the_rings, lala_land]
fresh_tomatoes.open_movies_page(movies)
