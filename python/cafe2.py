# Starbucks reboot using functions

import datetime
import time

def take_order(is_first, name):
    """ This functions takes order from user. Takes a boolean operator to determine if the order is the first order. It returns it as a string."""
    if is_first:
        order = input(f"Hi, {name}! What would you like to order? ")


    else: 
        order = input(f"Anything else, {name}? ")

    return order


def is_menu_item(item):
    """Predicate that returns true if item is on the menu."""

    menu = {
        "latte":4.95,
        "water":2.00,
        "muffin":3.00,
        "bagel":3.50,
        "cake pop":3.50,
        "americano":4.00
    }

    is_on_menu = False

    if item in menu:
        is_on_menu = True

    return is_on_menu
    



    
final_order = []


print("Welcome to Cafe. ")
name = input("What's your name? ")

answer = take_order(True, name)

if is_menu_item(answer):
    final_order.append(answer)
else:
    print("That's not on the menu")

while answer != "no": 
    answer = take_order(False, name)
    
    if is_menu_item(answer):
        final_order.append(answer)
    else:
        print("That's not on the menu")


    #print(final_order)
number_of_items = len(final_order)
print(f"You ordered {number_of_items} items." )
print(", ".join(final_order))

from datetime import date
print(date.today())



