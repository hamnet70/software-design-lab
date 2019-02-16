# Prints two lines as typed. The three single quotes extend the print command across the lines.
print('''Mary had a little lamb
it's fleece was white as snow''')

# Prints the string
print("hello world")

# print(x)--this was our traceback error

# Defines the list flowers with three items in it
flowers = ['rose', 'violet', 'buttercup']

# print(flowers)

# Creates a for-loop that, for each item in the list, prints the item
for flower in flowers:
    print(flower)

# Creates a for-loop that, for each item in the list, prints a string within a string
for x in flowers:
    
    print('I like %s' %x)
    