# This line sets the variable x to a string with a decimal formatted value of 10
x = "There are %d types of people." % 10
# This line sets the variables binary and do not to strings
binary = "binary"
do_not = "don't"
# This line sets the var y to a string with two string formatted values corresponding to variables
y = "Those who know %s and those who %s." % (binary, do_not)

# These two lines print the variables x and y
print(x)
print(y)

# These two lines quote the quotes using formated values of "everything" and string
print("I said: %r." % x)
print("I also said: '%s'." % y)

# These lines set up two variables, one to a false evaluation and the other to a string with an everything format
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# This line prints the variable joke_evaluation inserting the returned false for the %r value
print(joke_evaluation % hilarious)  

# These two lines assign strings to variables w and e
w = "This is the left side of..."
e = "a string with a right side."

# This line prints the variables w and e side by side, concatenating them
print(w + e)
