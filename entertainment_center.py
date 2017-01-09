import fresh_tomatoes
import media

# Below are the movie listings
ex_machina = media.Movie("Ex Machina",
                         "AI frees itself from the research lab",
                         "http://www.terry-posters.com/data/products/avatars/31107/watermarked/ex_machina_dvd.jpg?1445955454",
                         "https://www.youtube.com/watch?v=PI8XBKb6DQk")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

forbidden_planet = media.Movie("Forbidden Planet",
                               "Watch out this planet is forbidden!",
                               "http://images.moviepostershop.com/forbidden-planet-movie-poster-1956-1010197456.jpg",
                               "https://www.youtube.com/watch?v=F17CCRoMttQ")

earth_stood_still = media.Movie("The Day The Earth Stood Still",
                                "Stand frozen and watch the UFO visit earth!",
                                "http://www.impawards.com/1951/posters/day_the_earth_stood_still_ver3_xlg.jpg",
                                "https://www.youtube.com/watch?v=OfpSXI8_UpY")
                                
matrix = media.Movie("The Matrix",
                     "Neo wakes up",
                     "http://thebitplayers.net/wp-content/uploads/2015/08/the-matrix-movie-poster.jpg",
                     "https://www.youtube.com/watch?v=tGgCqGm_6Hs")

aliens = media.Movie("Aliens",
                     "Aliens on an Alien Planet",
                     "https://fanart.tv/fanart/movies/679/movieposter/aliens-52247dccb14ff.jpg",
                     "https://www.youtube.com/watch?v=XKSQmYUaIyE")

# The movies are bundled into a list
movies = [ex_machina, avatar, forbidden_planet, earth_stood_still, aliens, matrix]

# The movie objects are shipped off to fresh_tomatoes for processing
fresh_tomatoes.open_movies_page(movies)



                     


