# This program is supposed to take a list and print out all of the elements under 5
import time

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

answer = input("Would you like to add a number to my list? y/n ")


while answer == "y":
    add_num = float(input("Type that number. "))
    a.append(add_num)
    answer = input ("Would you like to add another number to my list? y/n ")

print("Here's my whole list:")
print(a)
time.sleep(1)

print("Here are all the numbers in my list under 5: ")

for elements in a:
    if elements < 5:
        print(elements)
        b.append(elements)

print("Here is my new list:")
print(b)




