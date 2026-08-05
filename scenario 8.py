#8. Movie Collection Management System, Develop a Python application to manage movie records.
# Movie Collection Management System

class Movie:
    def __init__(self, name, rating, price):
        self.name = name
        self.rating = rating
        self.price = price

 
    def category(self):
        if self.rating >= 8:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\nMovie Details")
        print("-" * 40)
        for movie in self.movies:
            print("Movie Name :", movie.name)
            print("Rating     :", movie.rating)
            print("Ticket Price: Rs.", movie.price)
            print("Category   :", movie.category())
            print("-" * 40)


cinema = Cinema()

# Add Movies
cinema.add_movie(Movie("Pushpa 2", 8.5, 250))
cinema.add_movie(Movie("Housefull 5", 6.8, 200))
cinema.add_movie(Movie("Movie X", 4.2, 150))

# Display Movies
cinema.display_movies()
