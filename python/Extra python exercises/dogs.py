# This program creates compares the ages of objects from the dog class


class Dog:

    species = "Mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    

dog_1 = Dog("Schuba", 10)
dog_2 = Dog("Sonny", 7)
dog_3 = Dog("Hank", 3)
dog_4 = Dog("Isis", 12)

#print(dog_2.name)
#print(f"{dog_1.name} is {dog_1.age}.")

def get_oldest(*ages):
    return max(ages)

print("The oldest dog is ")
print(str(get_oldest(dog_1.age, dog_2.age, dog_3.age, dog_4.age)))