# This program allows a user to generate a list of seats available in a one-story theater, to create lists of premium, available, 
# and unavailable seats, and to generate prices. Note that, for now, rows is limited to 26


def gen_seats(row_letter, seats_in_row):

    seats = []

    def row_range(c1, c2):
        """Generates the characters from `c1` to `c2`, inclusive."""
        for c in range(ord(c1), ord(c2)+1):
            yield chr(c)

    seat_num = 1

    while seat_num != seats_in_row:
        for x in row_range('a', str(row_letter)):
            seats.append(x+str(seat_num))
        seat_num += 1

    return seats


def is_premium(seat_num, user_seats_in_row):
    if seat_num[0] == "a" or seat_num[0] == "b" or seat_num[1] == str(user_seats_in_row) or seat_num[1] == "1":
        return true
    else:
        return false


user_last_row = str(input("What is the last letter of rows in your theater? "))
user_seats_in_row = int(input("How many seats in each row in your theater? ")) + 1

print("Here are your theater's seats: ")
print(gen_seats(user_last_row, user_seats_in_row))

seat_num = input("Type in your seat number to determine if it is a premium seat (ex. a4): ")

if is_premium:
    print(f"Seat number {seat_num} is a premium ticket.")
else: print(f"Seat number {seat_num} is not a premium ticket. Bring binoculars.")