# This is just to practice creating a class with methods and attributes

# This line defines my class
class student:

#This is a class variables that live outside of the individual initiations of students
    num_of_students = 0
    extra_credit = .1

# This line definites the initiation of a given instance. It is, if I understand correctly, a method that defines class attributes
    def __init__(self, first, last, section, gpa):
        self.first = first
        self.last = last
        self.section = section
        self.gpa = gpa
        self.email = first + "." + last + "@chapin.edu"

#This line adds to the number of students when each instance of the class is created
        student.num_of_students += 1

# This line defines a method that works on each instance to return the concatenated first and last attributes
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_extra_credit(self):
        self.gpa = float(self.gpa + self.extra_credit)


student_1 = student("Amelia", "Barnum", "W", 3.8)
student_2 = student("Marguerite", "Morris", "W", 4.0)
student_3 = student("Taylor", "Bakare", "W", 4.0)
student_4 = student("Emani", "Babb", "Y", 3.4)
student_5 = student("Maddy", "Machare", "Y", 3.5)

# The below were test print statements.
#print(student_5.email)
#print(student_1.first)
#print(student_4.section)
#print(student_2.fullname())
#print("There are now %d students in this database." % student.num_of_students)

print(student_4.gpa)

student_4.apply_extra_credit()

print(student_4.gpa)

