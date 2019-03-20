# This simple function splits into three variables the passed three-term string that is joined by hyphens. It then prints a string
# joining those variables in a full sentence. Cool.

#def split_string(given_string):
#    first, last, section = given_string.split("-")
#    print(f"{first} {last} is in section {section}.")

#split_string("Taylor-Bakare-W")
#split_string("Amelia-Barnum-W")
#split_string("Maddie-Blanco-Y")

import datetime

def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
        return False
    else:
        return True

my_date = datetime.date(2019, 3, 16)

if is_workday(my_date):
    print(f"Yes, {my_date} is a workday.")
else:
    print(f"No, {my_date} is not a workday.")






