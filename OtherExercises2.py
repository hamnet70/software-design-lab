# This line creates the var question and gives it a string value of "What is your..."
question = "What is your favorite tv show?"

# This line displays that string to the user
print(question)
# This line creates the var answer and assigns whatever the user types on the next line
answer = input()

# This line prints a string that inserts the users answer into it
print("You watch %s! I love that show!" % answer)


question = "What is your favorite food?"

print(question)
answer = input()

print("You eat %s! I love that too!" % answer)


# This line displays a question to the user (I skipped setting a variable to it)
print("What is your lucky number?")
# This line creates var response and assigns to it what the reader types
response = input()

# This line creates the var number and assigns it the integer value of that the user typed
# The user response must be an integer anyway; they cannot type 'ten' without getting an error
number = int(response)
# This line creates var plusTen and adds ten to the integer value now stored as number
# This ine could be eliminated if number were defined as int(reponse) + 10, but then you couldn't
# use the original "lucky number" later.
plusTen = number + 10
plusTwenty = number + 20

# This line displays a string to the user and concatenates it with the string value of the
# integer plusTen
print("Add 10 to that and you get " + str(plusTen))
print("If we add 10 to that, we get ", plusTen)
print("If we add 10 to that, we get %s" % plusTen)
print("If we add 10 or 20 to that, we get %s and %s respectively" % (plusTen, plusTwenty))

