## This program calculates a hotel bill based on room size, stay length, and taxes

import time

k = 120.00
q = 100.00
d = 80.00

answer = input("Are you ready to checkout? y / n")

if answer=="n":
    print("Enjoy the rest of your stay.")
    exit()


print("Wonderful.")
time.sleep(1)
room_type = input("What room did you have? King (k), queen (q), or double (d)?")

if room_type == "k":
    base_cost = 120.00
elif room_type == "q":
    base_cost = 100.00
elif room_type == "d":
    base_cost = 80.00
else:
    print("You didn't type in a valid room type, so this program will end.")
    exit()

time.sleep(2)
stay = input("How many nights did you stay?")

total_cost = (base_cost * float(stay)) * 1.05
print("Room rate = $%d/per night." %base_cost)
time.sleep(2)
print("You stayed for %s night(s)." %float(stay))
time.sleep(2)
print("Your bill comes to $%s." % total_cost)






