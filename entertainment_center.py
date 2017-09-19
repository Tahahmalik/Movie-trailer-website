# import the required classes and modules to run this application

import Media
import fresh_tomatoes

# Create instances of Media class by adding movies to be displayed on webpage

Moana = Media.Movie(
    "Moana",
    "https://upload.wikimedia.org/wikipedia/en/thumb/2/26/Moana_Teaser_Poster.jpg/220px-Moana_Teaser_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=LKFuXETZUsI"
	)

Themummy = Media.Movie(
    "The Mummy",
    "https://upload.wikimedia.org/wikipedia/en/a/a2/The_Mummy_%282017%29.jpg",
    "https://www.youtube.com/watch?v=IjHgzkQM2Sg"
    )

Legomovie = Media.Movie(
    "The Lego Batman Movie",
    "https://upload.wikimedia.org/wikipedia/en/6/61/The_Lego_Batman_Movie_PromotionalPoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=rGQUKzSDhrg"
    )

Diverted = Media.Movie(
    "Diverted",
    "https://upload.wikimedia.org/wikipedia/en/6/60/Diverted.jpg",
    "https://www.youtube.com/watch?v=9U3pKQbtuWE"
    )

# Add movies to array in order to be passed as argument to fresh_tomatoes.open_movies_page # NOQA
movies = [
    Moana,
    Themummy,
    Legomovie,
    Diverted
    ]

# Pass movies array to fresh_tomatoes as an argument
fresh_tomatoes.open_movies_page(movies)
