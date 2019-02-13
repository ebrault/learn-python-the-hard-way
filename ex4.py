# Defines cars and sets it to 100
cars = 100
# Defines space_in_a_car and sets it to 4.0
space_in_a_car = 4
# Defines drivers and sets it to 30
drivers = 30
# Defines passengers and sets it to 90
passengers = 90
# Defines cars_not_driven as the difference between ars and drivers (70)
cars_not_driven = cars - drivers
# Defines cars_driven as aliased to drivers (30)
cars_driven = drivers
# Defines carpool_capacity and sets it to cars_driven * space_in_a_car (120.0)
carpool_capacity = cars_driven * space_in_a_car
# Defines average_passengers_per_car an sets it to the quotient of passengers and cars driven (3)
average_passengers_per_car = passengers / cars_driven

# Prints the strings concatenated with the value of cars in between
print "There are", cars, "cars available."
# Prints the strings concatenated with the value of drivers in between
print "There are only", drivers, "drivers available."
# Prints the strings concatenated with the value of cars_not_driven in between
print "There will be", cars_not_driven, "empty cars today."
# Prints the strings concatenated with the value of carpool_capacity in between
print "We can transport", carpool_capacity, "people today."
# Prints the strings concatenated with the value of passengers in between
print "We have", passengers, "to carpool today."
# Prints the strings concatenated with the value of average_passengers_in_car in betwen
print "We need to put about", average_passengers_per_car, "in each car."
