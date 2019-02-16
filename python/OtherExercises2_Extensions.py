# I am making all of the below up, trying to both practice and extend the concepts I learned in the wikibook
#    Python lessons

# Displays a string to the user asking her name and assigns her answer to the var name
print("Hi. What's your name?")
name = input()

# Displays a new string to the user asking her age, assigns her answer to the var number, assigns the integer
#   value of her answer to the var age, then stores in var age_comparison the difference between her age and 48
print("How old are you?")
number = input()
age = int(number)
age_comparison = 48 - age

if age > 48:
    print("You are older than I am.")
elif age < 48:
    print("You are younger than I am.")
else:
    print("We are the same age!")

# Displays a new string to the user asking where she was born. Assigns her answer to var birthplace
print("Where were you born?")
birthplace = input()

# Invokes the ability to track time
import time

# Displays a string within a string that greets the user with her name, then pauses for two seconds
print("Well, %s, it's nice to meet you" % name)
time.sleep(2)

# Displays a number within a string, responding and comparing the user's age to mine, then waits five seconds
print("My name's Kelly. I'm 48, so we are %d years apart." % age_comparison)
time.sleep(5)

# Displays a string within a string noting that I've never been to her birth place.
print("I don't believe I've ever been to %s." % birthplace)

print("I like the sound of your name.")
time.sleep(3)

print((name + " ") *100)
time.sleep(3)

print("Yeah. That sounds nice.")