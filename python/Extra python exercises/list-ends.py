# This program prints out the first and last items of any given list
# I added extra challenge by allowing the user to add to the list

import time

sodas = ["Pepsi", "Canada Dry", "Fanta"]

print("Here's what's on my list:" )
time.sleep(1)
print(sodas)
time.sleep(1)
response = input("Would you like to add a brand? y/n ")

while response == "y":
    add = input("Add a brand: ")
    sodas.append(add)
    time.sleep(1)
    response = input("Would you like to add another brand? y/n ")
    time.sleep(1)

last = len(sodas)

print("The first item on this list is " + sodas[0])


print("The last item on this list is " + sodas[last-1])




