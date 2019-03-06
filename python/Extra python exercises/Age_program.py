# This program is supposed to ask a user her name and age, and then tell her what year she will turn 100.
# I am going to ignore the obvious flaw in this program: that someone's age is not year dependent, but month and year dependent.

import time

name = input("What is your name?")
time.sleep(1)
age = int(input("How old are you? (number only, please)"))
time.sleep(1)

year_100 = (100 - int(age)) + 2019

print(name + " will turn 100 in " + str(year_100))


