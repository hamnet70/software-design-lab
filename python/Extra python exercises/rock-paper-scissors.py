# This is a two-player rock-paper-scissors game, which seems kind of lame, but whatever.

import time

player_1 = input("Enter player 1's name: ")
time.sleep(1)
print("Hello, %s." % player_1)
time.sleep(1)

player_2 = input("Enter player 2's name: ")
time.sleep(1)
print("Hello, %s." % player_2)
time.sleep(1)

answer = input("Do you want to play rock, paper, scissors? y/n ")
time.sleep(1)

while answer == "y":
    player_1_answer = input("%s, rock (r), paper (p), or scissors? " % player_1)
    player_2_answer = input("%s, rock (r), paper (p), or scissors? " % player_2)
    if player_1_answer == player_2_answer:
        answer = input("It's a tie. Do you want to play again? y/n ")
    elif player_1_answer == "r" and player_2_answer == "p":
        answer = input("%s wins. Do you want to play again? y/n " % player_2)
    elif player_1_answer == "r" and player_2_answer == "s":
        answer = input("%s wins. Do you want to play again? y/n" % player_1)
    elif player_1_answer == "p" and player_2_answer == "r":
        answer = input("%s wins. Do you want to play again? y/n" % player_1)
    elif player_1_answer == "p" and player_2_answer == "s":
        answer = input("%s wins. Do you want to play again? y/n" % player_2)
    elif player_1_answer == "s" and player_2_answer == "r":
        answer = input("%s wins. Do you want to play again? y/n" % player_2)
    else:
        answer = input("%s wins. Do you want to play again? y/n" % player_1)

print("Thanks for playing!")