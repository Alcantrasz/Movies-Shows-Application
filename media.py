# Improved Program #
####################
class Media:
    """Represents a Movie or Show."""

    ALLOWED_TYPES = ["Movie", "Show"]

    ALLOWED_GENRES = [
        "Action",
        "Comedy",
        "Drama",
        "Horror",
        "War",
        "Documentary"
    ]

    ALLOWED_RATINGS = [1, 2, 3, 4, 5]

    def __init__(self, media_type, name, genre, rating):
        media_type = media_type.capitalize()
        genre = genre.capitalize()

        # Validation
        if media_type not in self.ALLOWED_TYPES:
            raise ValueError(
                f"Type must be one of: {', '.join(self.ALLOWED_TYPES)}"
            )

        if genre not in self.ALLOWED_GENRES:
            raise ValueError(
                f"Genre must be one of: {', '.join(self.ALLOWED_GENRES)}"
            )

        try:
            rating = int(rating)
        except ValueError:
            raise ValueError("Rating must be a number between 1 and 5.")

        if rating not in self.ALLOWED_RATINGS:
            raise ValueError("Rating must be between 1 and 5.")

        if not name.strip():
            raise ValueError("Please enter a name.")

        self.media_type = media_type
        self.name = name.title().strip()
        self.genre = genre
        self.rating = rating

    def to_tuple(self):
        """Returns the object as a tuple for SQLite insertion."""
        return (
            self.media_type,
            self.name,
            self.genre,
            self.rating
        )

    def __repr__(self):
        return (
            f"Media("
            f"type='{self.media_type}', "
            f"name='{self.name}', "
            f"genre='{self.genre}', "
            f"rating={self.rating})"
        )







# My Program #
##############
"""
class Movie: 

    ALLOWED_GENRES = [ "Action", "Comedy", "Drama", "Horror", "War", "Documentary" ] 

    ALLOWED_RATINGS = [ "1", "2", "3", "4", "5" ] 
    
    def __init__(self, movie_genre, movie_name, movie_rating): 

        normalized_genre = movie_genre.capitalize() 
        normalized_rating = movie_rating

        if normalized_genre not in self.ALLOWED_GENRES: 
            raise ValueError(f"Please type: {self.ALLOWED_GENRES}") 

        if normalized_rating not in self.ALLOWED_RATINGS: 
            raise ValueError(f"Please type: {self.ALLOWED_RATINGS}") 

        self.movie_genre = normalized_genre
        self.movie_name = movie_name
        self.movie_rating = normalized_rating 


class Show: 

    ALLOWED_GENRES = [ "Action", "Comedy", "Drama", "Horror", "War", "Documentary" ] 

    ALLOWED_RATINGS = [ "1", "2", "3", "4", "5" ] 
    
    def __init__(self, show_genre, show_name, show_rating): 

        normalized_genre = show_genre.capitalize() 
        normalized_rating = show_rating 

        if normalized_genre not in self.ALLOWED_GENRES: 
            raise ValueError(f"Please type: {self.ALLOWED_GENRES}") 

        if normalized_rating not in self.ALLOWED_RATINGS: 
            raise ValueError(f"Please type: {self.ALLOWED_RATINGS}") 

        self.show_genre = normalized_genre
        self.show_name = show_name
        self.show_rating = normalized_rating 


saved_movies = [] 
saved_shows = [] 

loop = input("Movie, Show, or Quit: ").capitalize() 

while True: 
    if loop == "Movie": 

        input_genre = input("Please write the Genre of the Movie: ") 
        input_movie = input("Please write the name of the Movie: ") 
        input_rating = input("The movies ranking can only be 1-5: ") 
        
        current_movie = Movie(movie_genre = input_genre, movie_name = input_movie, movie_rating = input_rating) 
        saved_movies.append([current_movie.movie_genre, current_movie.movie_name, current_movie.movie_rating]) 

        print(saved_movies) 
        loop = input("Movie, Show, or Quit: ").capitalize() 

        if loop == "Quit": 
            raise SystemExit 
            
    elif loop == "Show": 

        input_genre = input("Please write the Genre of the Show: ") 
        input_show = input("Please write the name of the Show: ") 
        input_rating = input("The movies ranking can only be 1-5: ") 
        
        current_show = Show(show_genre = input_genre, show_name = input_show, show_rating = input_rating) 
        saved_shows.append([current_show.show_genre, current_show.show_name, current_show.show_rating]) 

        print(saved_shows) 
        loop = input("Movie, Show, or Quit: ").capitalize() 

        if loop == "Quit": 
            raise SystemExit
"""