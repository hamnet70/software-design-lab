# This program is supposed to tell a user if the number they input was even or odd

import time

print("Hello, there.")
time.sleep(1)
name = input("What's your name?")
time.sleep(1)
number = int(input("Type a whole number, and I'll tell you if it is odd or even."))

if (number % 2 == 0):
    print ("Well, %s, your number is even." % name)
    if (number % 4 == 0):
            print("And heck! It's even a multiple of 4!")
else:
    print("Well, %s, your number is odd. But you're not." % name)