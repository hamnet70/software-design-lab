# This program attempts to use classes to set up a virtual theater of any of three levels with various pricing, capacity, and premium status.

class seats:

    def __init__(self, row, seat_no):
        self.row = row
        self.seat_no = seat_no
        #self.location = self.name + " " + str(row) + str(seat_no)
        self.location = "{} {}{}".format(self.name, str(row), str(seat_no))
        self.is_available = "Available"

    def is_purchased(self):
        self.is_available = "Sold"

    def is_returned(self):
        self.is_available = "Available"


class orchestra(seats):

    name = "Orchestra"
    price = 125

    def __init__(self, row, seat_no, seating_cap=None):
        super().__init__(row, seat_no)


class mezz(seats):

    name = "Mezzanine"
    price = 75

    def __init__(self, row, seat_no, seating_cap=None):
        super().__init__(row, seat_no)
        

class balcony(seats):

    name = "Balcony"
    price = 50

    def __init__(self, row, seat, seating_cap=None):
        super().__init__(row, seat)


# Working on this section
#def seating_cap(level):
#    row_max = input("Assuming your first row of seats is row a, what letter is the last row of seats? (Currently, this program can only take up to letter z:  "))
#    seat_max = input("How many seats are there per row? "))
    


        



    

# All of the code below is just for testing
orchestra_1 = orchestra("a", 4)
mezz_1 = mezz("b", 4)
balcony_1 = balcony("f", 9)


#print(orchestra_1.location)
#(orchestra_1.price)
#(orchestra_1.is_available)
#(mezz_1.location)
#(mezz_1.price)
#(mezz_1.is_available)
#(balcony_1.location)
#(balcony_1.price)
#(balcony_1.is_available)

orchestra_1.is_purchased()

#(orchestra_1.location)
#(orchestra_1.price)
#(orchestra_1.is_available)
#(mezz_1.location)
#(mezz_1.price)
#(mezz_1.is_available)
#(balcony_1.location)
#(balcony_1.price)
#(balcony_1.is_available)




