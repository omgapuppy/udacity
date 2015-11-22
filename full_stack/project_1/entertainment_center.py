import fresh_tomatoes
import media
# Create movie instances by calling init in Movie class in media.py
# Each movie's variables are passed when calling init
guardians_galaxy = media.Movie("Guardians of the Galaxy",
                                "Awesome space raccoon shooting stuff",
                                "http://cdn.collider.com/wp-content/uploads/guardians-of-the-galaxy-poster-star-lord.jpg",
                                "https://www.youtube.com/watch?v=89yh3vYs-zo")

avatar = media.Movie("Avatar",
                     "Naked blue aliens, being all hippy",
                     "http://www.goldposter.com/wp-content/uploads/2015/05/Avatar_poster_goldposter_com_56.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

fast_furious = media.Movie("Furious 7",
                           "Paul Walker's dead :(",
                           "http://cdn2-www.comingsoon.net/assets/uploads/2015/02/Furious7onelastposterbig.jpg",
                           "https://www.youtube.com/watch?v=Skpu5HaVkOc")

star_wars = media.Movie("Star Wars: Episode VII - The Force Awakens",
                        "New, hope JJ doesn't mess it up",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/10/star-wars-force-awakens-official-poster.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

martian = media.Movie("The Martian",
                      "Matt Damon in space",
                      "http://www.screenrelish.com/wp-content/uploads/2015/08/The-Martian-Launch-One-Sheet.jpg",
                      "https://www.youtube.com/watch?v=Ue4PCI0NamI")

gravity = media.Movie("Gravity",
                      "Dr. Ryan Stone (Sandra Bullock) is a medical engineer on her first shuttle mission.",
                      "http://cdn3-www.comingsoon.net/assets/uploads/1970/01/file_582992_gravity-poster-clooney.jpg",
                      "https://www.youtube.com/watch?v=OiTiKOy59o4")
# Create array of movies to be displayed on web page
movies = [guardians_galaxy, avatar, fast_furious, star_wars, martian, gravity]
# Call open_movies_page in fresh_tomatoes.py and pass array of movies
fresh_tomatoes.open_movies_page(movies)
