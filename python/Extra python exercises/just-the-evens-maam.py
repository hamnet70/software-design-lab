# This program creates a list of only even numbers from a given list.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [item for item in a if item % 2 == 0]

#for item in a:
#    if item % 2 == 0:
#        b.append(item)

print(b)
