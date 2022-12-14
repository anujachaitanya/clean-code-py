import unittest
from src.Customer import Customer
from src.Movie import Movie
from src.Rental import Rental


class TestCustomer(unittest.TestCase):
    def test_should_return_valid_statement_for_different_movie_price_codes(self):
        customer = Customer("John")
        movie1 = Movie("DDLJ", 1)
        movie2 = Movie("K3G", 2)
        movie3 = Movie("Devdas",0)
        customer.add_rental( Rental(movie1, 12))
        customer.add_rental(Rental(movie2, 30))
        customer.add_rental(Rental(movie3, 30))
        self.assertEqual(customer.statement(), "Rental Record for John\n\tDDLJ\t36\n\tK3G\t42.0\n\tDevdas\t44.0\nAmount owed is 122.0\nYou earned 4 frequent renter points")


if __name__ == '__main__':
    unittest.main()
