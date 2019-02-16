# This sets up the variable formatter with three raw data bits of info
formatter = "%r %r %r %r"

# This prints 1234
print(formatter % (1, 2, 3, 4))
# This prints one two three four
print(formatter % ("one," "two", "three", "four"))
# This prints True False True False
print(formatter % (True, False, True, False))
# This prints %r %r %r %r (I think)
print(formatter % (formatter, formatter, formatter, formatter))
# This should print these all in a line, despite the spacing here?
print(formatter % (
    "I had this thing",
    "That you could type up right",
    "But it didn't sing", 
    "So I said goodnight."
))