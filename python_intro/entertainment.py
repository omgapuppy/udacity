import media

guardians_galaxy = media.Movie("Guardians of the Galaxy",
                                "Awesome space raccoon shooting shit",
                                "http://cdn.collider.com/wp-content/uploads/guardians-of-the-galaxy-poster-star-lord.jpg",
                                "https://www.youtube.com/watch?v=6lVH3ogPE0w")

print(guardians_galaxy.storyline)

avatar = media.Movie("Avatar",
                    "Naked blue aliens, being all hippy",
                    "http://www.goldposter.com/wp-content/uploads/2015/05/Avatar_poster_goldposter_com_56.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
print(avatar.storyline)
avatar.show_trailer()
