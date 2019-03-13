# This program allows a user to add to or retrieve from a dictionary of birthdays

import time

birthdays = {
    "Kelly":"August 5",
    "Hasib":"June 13",
    "Martha":"November 19",
    "Chris":"October 19:",
    "Josh":"December 13",
    "Geoffrey":"July 4",
    "Annie":"May 4",
    "Minna":"December 14",
}

answer_1 = input("Would you like to add (a) a birthday, retrieve (r) one, or exit (e)?  ")

while answer_1 != "e":
    if answer_1 == "a":
        name = input("Type in birthday person's name:  ")
        date = input("Type in the month and day (ex January 1):  ")
        birthdays[name]=date
    elif answer_1 == "r":
        name = input("Whose birthday would you like to know?  ")
        if name in birthdays:
            print(birthdays[name])
        else:
            print("That name is not in the dictionary as you have typed it.")
    answer_1 = input("Would you like to add (a), retrieve (r), or exit (e)?  ")





        




