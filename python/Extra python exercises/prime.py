# This program determines if a user-provided number is prime

number = int(input("Please enter any number.  "))

divisors = [2, 3, 5, 7]
factor = []
hit = 0

for x in divisors:
    if number % x == 0:
        # print("Not a prime. Your number is divisible by %d." % x)
        factor.append(x)
        hit += 1

if hit == 0 or number == 2 or number == 3 or number == 5 or number == 7:
    print("%d is a prime number!" % number)
else:
    print ("%d is not a prime number." % number)
    print ("It is divisible by:")
    print (factor)



