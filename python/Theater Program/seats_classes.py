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
        
    

# All of the code below is just for testing
orchestra_1 = orchestra("a", 4)
mezz_1 = mezz("b", 4)
balcony_1 = balcony("f", 9)


print(orchestra_1.location)
print(orchestra_1.price)
print(orchestra_1.is_available)
print(mezz_1.location)
print(mezz_1.price)
print(mezz_1.is_available)
print(balcony_1.location)
print(balcony_1.price)
print(balcony_1.is_available)

orchestra_1.is_purchased()

print(orchestra_1.location)
print(orchestra_1.price)
print(orchestra_1.is_available)
print(mezz_1.location)
print(mezz_1.price)
print(mezz_1.is_available)
print(balcony_1.location)
print(balcony_1.price)
print(balcony_1.is_available)




