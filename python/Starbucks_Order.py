# Trying to imitate the Starbucks receipt

# Imports the library random
import random

# Defines a list called order
order = []

# Creates a variable assigned to the user's prompted name
name = input("What's your name?  ")

# Defines a list of strings that could be used to say goodbye to the customer
thanks = ['Come again!', 'Hope you enjoy your order!', 'Remember, we are everywhere!', 
'Hope we did not overcharge you!']


# Creates a var item set to the user input
item = input("What would you like to order, %s?  " % name)
# Adds the item to the list
order.append(item)

# Creates a var response assigned to user input (prompted to be y or n)
response = input("Want anything else? y/n  ")

# Creates a loop that, as long as the user response is y (for yes I want another item), prompts for the item 
# and adds it to the list
while response == "y":
    item = input("What would you like to order?  ")
    order.append(item)
    response = input("Anything else? y/n  ")

# Prints the user's name in the string "user name's order"
print("%s's order:" % name)

# Uses a for loop to print each item in the list, regardless of the number of items
for x in order:
    print(x)

# Prints a random string from the list thanks
print(random.choice(thanks))











