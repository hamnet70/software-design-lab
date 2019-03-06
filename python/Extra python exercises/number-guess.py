# This game asks a user to guess a random number between 1 - 9

import random
import time
number_set = list(range(1, 101))
#I looked up how to do automatically create a list with a range, so I removed the line below and later set the range to 101.
#number_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
guesses = 1

print(number_set)

print("Welcome to the number guessing game.")
time.sleep(1)
print("If you want to quit at any time, type exit.")
time.sleep(1)
guess = (input("Pick a number between 1 and 100.   "))


x = random.choice(number_set)

while guess != "exit":
    if int(guess) == x:
        print("You got it! It took you %d guesses." % guesses)
        guess = input("If you want to play again, pick a new number between 1 and 100. Or type exit.   ")
        guesses = 1 
        x = random.choice(number_set)
        time.sleep(1)
        
    elif int(guess) > x:
        guess = input("Lower. Try again or type exit.   ")
        guesses += 1
    else:
        guess = input("Higher. Try again or type exit.   ")
        guesses += 1



