# This is just to see if I can create automatically generated lists of seats in a theater

# Step 1: Can I auto-generate a list of seats with rows and numbers

seats = []
premium_seats = []

# realize I don't need the next four lines, as I could append numerically
# def generate_seats(row, seat):
# seat_range = range(1, 11, 1)
# for x in seat_range:
#    print(x)

#I found the code below that produce a range of alphabetic characters
def row_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

seat_num = 1

while seat_num !=11:
    for x in row_range('a', 't'):
        seats.append(x+str(seat_num))
    seat_num += 1

print(seats)

for x in seats:
    if x[0] == "a" or x[0] == "t" or int(x[1]) < 6:
        premium_seats.append(x)

print(f"The premium seats are: {premium_seats}.")





    

