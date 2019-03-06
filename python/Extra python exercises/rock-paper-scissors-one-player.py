# This is a two-player rock-paper-scissors game, which seems kind of lame, but whatever.

import time
import random

player_1 = input("Enter your name: ")
time.sleep(1)
print("Hello, %s." % player_1)
time.sleep(1)
poss = ["r", "p", "s"]


answer = input("Do you want to play rock, paper, scissors? y/n ")
time.sleep(1)

while answer == "y":
    player_1_answer = input("%s, rock (r), paper (p), or scissors? " % player_1)
    player_2_answer = random.choice(poss)
    if player_1_answer == player_2_answer:
        answer = input("It's a tie. Do you want to play again? y/n ")
    elif player_1_answer == "r" and player_2_answer == "p":
        answer = input("The computer chose paper, so it wins. Do you want to play again? y/n ")
    elif player_1_answer == "r" and player_2_answer == "s":
        answer = input("%s wins. Do you want to play again? y/n" % player_1)
    elif player_1_answer == "p" and player_2_answer == "r":
        answer = input("%s wins. Do you want to play again? y/n" % player_1)
    elif player_1_answer == "p" and player_2_answer == "s":
        answer = input("The computer chose scissors, so it wins. Do you want to play again? y/n" )
    elif player_1_answer == "s" and player_2_answer == "r":
        answer = input("The computer chose rock, so it wins. Do you want to play again? y/n" )
    else:
        answer = input("%s wins. Do you want to play again? y/n" % player_1)

print("Thanks for playing!")