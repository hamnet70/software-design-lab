# This is just to practice creating a class with methods and attributes

# This line defines my class
class student:

#These are class variables that live outside of the individual instantiations of students
    num_of_students = 0
    extra_credit = .1


# This line defines the initiation of a given instance. It is, if I understand correctly, a method that defines class attributes
    def __init__(self, first, last, section, gpa):
        self.first = first
        self.last = last
        self.section = section
        self.gpa = gpa
        self.email = first + "." + last + "@chapin.edu"

#This line adds to the number of students when each instance of the class is created
        student.num_of_students += 1

# This line defines a method that works on each instance to return the concatenated first- and last-name attributes
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_extra_credit(self):
        self.gpa = float(self.gpa + self.extra_credit)



class workshop(student):
    extra_credit = 1.5
    num_of_ex_time_students = 0

    def __init__(self, first, last, section, gpa, ex_time):
        super().__init__(first, last, section, gpa)
        self.ex_time = ex_time
        workshop.num_of_ex_time_students += 1

student_1 = student("Amelia", "Barnum", "W", 3.8)
student_2 = student("Marguerite", "Morris", "W", 4.0)
student_3 = student("Taylor", "Bakare", "W", 4.0)
student_4 = student("Emani", "Babb", "Y", 3.4)
student_5 = student("Maddy", "Machare", "Y", 3.5)
workshop_1 = workshop("Natalie", "Delk", "X", 3.5, "Yes")



# The below were test print statements.
# print(student_5.email)
# print(student_1.first)
# print(student_4.section)
# print(student_2.fullname())

# I updated this line after our class to emply the f {} approach to inserting variables into strings. So fun!
print(f"There are now {student.num_of_students} students in this database.")

print(f"Maddy's gpa is {student_5.gpa}")
print(f"Natalie's gpa is {workshop_1.gpa}")

student_5.apply_extra_credit()
workshop_1.apply_extra_credit()

print(f"Maddy's gpa is now {student_5.gpa}")
print(f"Natalie's gpa is now {workshop_1.gpa}")

print(f"Does Natalie get extended time? Answer: {workshop_1.ex_time}.")
print(f"There are now {workshop.num_of_ex_time_students} extra-time students in the class. ")



