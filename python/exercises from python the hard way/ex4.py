#Sets up the variables for cars, space, drivers, and passengers with fixed numbers
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

#Sets up variables with calculations of variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#Prints values in strings
print("There are ", cars, " cars available.")
print("There are only ", drivers, " drivers available.")
print("There will be ", cars_not_driven, " empty cars today.")
print("We can transport ", carpool_capacity, " people today.")
print("We have ", passengers, " to carpool today.")
print("We need to put about ", average_passengers_per_car, " in each car.")