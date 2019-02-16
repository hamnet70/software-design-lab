# Practicing the use of three single quotes to extend the print command over several lines
# I added spaces for dramatic effect and like it
print('''


Let me not to the marriage of true minds
Admit impediments. Love is not love
Which alters when it alteration finds
Nor bends with the remover to remove.


''')
import time

# Defining a list of poets

poets = ['Shakespeare', 'Clifton', 'Dickinson', 'cummings', 'Heaney', 'Frost']

print("Let's think about poets.")
time.sleep(3)

# Setting up a for-loop that asks the advertising question of whether you have that poet

for x in poets:
    print("Got %s?" %x)
    time.sleep(3)

# Asks the user to add a poet and sets the var added to that response
added = input("Whom did I forget? ")

# Adds the user's suggestion to the list
poets.append(added)

# Repeats the print loop of the list, which now includes the user's addition
for x in poets:
    print("Got %s?" %x)

response = input("Can you name any other poets? y/n ")

while response == "y":
    added = input("Ok, name one. ")
    poets.append(added)
    response = input("Can you name another? y/n ")

number = (len(poets)-6)

if number <= 1:
    print("Really? You don't know any other poets?")
elif number <= 3:
    print("That's not very many. You should check out poets.org")
elif number <= 6:
    print("Not bad. You knew %d poets." %number)
elif number >=7:
    print("Wow! You know a ton!")


    




