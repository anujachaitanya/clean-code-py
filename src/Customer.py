class Customer:
    def __init__(self, name):
        self.__name = name
        self.__rentals = []

    def add_rental(self, arg):
        self.__rentals.append(arg)

    def get_name(self):
        return self.__name

    def total_rental_amount(self):
        total_amount = 0   
        for rental in self.__rentals:
            total_amount += rental.amount()
        return total_amount
    
    def total_frequent_renter_points(self):
        frequent_renter_points = 0
        for rental in self.__rentals:
            frequent_renter_points += rental.rental_points()
        return frequent_renter_points

    def text_statement(self): 
        statement = "Rental Record for " + self.get_name() + "\n"
        for rental in self.__rentals:
            statement += "\t" + rental.get_movie().get_title() + "\t" + str(rental.amount()) + "\n"
            
        total_amount = self.total_rental_amount()

        statement += "Amount owed is " + str(total_amount) + "\n"
        statement += "You earned " + str(self.total_frequent_renter_points()) + " frequent renter points"
        return statement
    
    def html_statement(self):
        statement = "<h1>Rental Record for " + self.get_name() + "</h1><br><p>"
        for rental in self.__rentals:
            statement += rental.get_movie().get_title() + "\t" + str(rental.amount()) + "<br>"
        
        total_amount = self.total_rental_amount()
                    
        statement += "Amount owed is " + str(total_amount) + "<br>"
        statement += "You earned " + str(self.total_frequent_renter_points()) + " frequent renter points</p>"
        return statement