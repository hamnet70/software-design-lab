# 11:22
# This program generates as many Fibonacci numbers as the user requests.

def Fibonacci(times):
    counter = 2
    sequence = [0, 1]
    if times == 0:
        return "Then why'd you run this program? "
    if times == 1:
        return sequence[0]
    while counter != times:
        sequence.append(sequence[-2] + sequence[-1])
        counter += 1
    return sequence

print(Fibonacci(int(input("How many Fibonnaci numbers would you like?"))))

