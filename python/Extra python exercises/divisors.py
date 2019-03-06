# This program is outputs the divisors of a user-given number

list = range(2,11)
new_list = []

number = int(input("Type in a whole number."))

for thing in list:
    if number % thing == 0:
        new_list.append(thing)

print("Your number has the following divisors: ")
print(new_list)

