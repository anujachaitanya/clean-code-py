from .Movie import Movie
class Rental:
    def __init__(self, movie, days_rented):
        self.__movie = movie
        self.__daysRented = days_rented

    def get_days_rented(self):
        return self.__daysRented

    def get_movie(self):
        return self.__movie
    
    def rental_points(self):
        rental_point = 1
        if self.__movie.get_price_code() == Movie.NEW_RELEASE and self.__daysRented > 1:
            rental_point += 1
        return rental_point
    
    def amount(self):
        amount = 0
        price_code = self.__movie.get_price_code()
        if price_code == Movie.REGULAR:
            amount += 2
            if self.__daysRented > 2:
                amount += (self.__daysRented - 2) * 1.5

        elif price_code == Movie.NEW_RELEASE:
            amount += self.__daysRented * 3

        elif price_code == Movie.CHILDREN:
            amount += 1.5
            if self.__daysRented > 3:
                amount += (self.__daysRented - 3) * 1.5
        return amount

