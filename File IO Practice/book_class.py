class Book:
    def __init__(self, movie, revenue):
        self.movie = movie
        self.revenue = revenue

    def __str__(self):
        return f"{self.movie} has a revenue of {self.revenue}"
