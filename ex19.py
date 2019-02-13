# Defines function cheese_and_crackers that takes the parameters cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints the string with the decimal formatter and inserts the value of the argument passed to cheese_count
    print "You have %d cheeses!" % cheese_count
    # Prints the string with the decimal formatter and inserts the value of the argument passed to boxes_of_crackers
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # Prints the string
    print "Man that's enough for a party!"
    # Prints the string with a newline
    print "Get a blanket.\n"

# Prints the string
print "We can just give the function numbers directly:"
# Calls cheese_and_crackers with 20 passed as an argument to cheese_count and 30 passed as an argument to boxes_of_crackers
cheese_and_crackers(20, 30)

# Prints the string
print "Or we can use variables from our script:"
# Defines the variable amount_of_cheese and sets it to 10
amount_of_cheese = 10
# Defines the variable amount_of_crackers and sets it to 50
amount_of_crackers = 50

# Calls cheese_and_crackers with amount_of_cheese and amount_of_crackers passed as arguments to cheese_count and boxes_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Prints the string
print "we can even do math inside too:"
# Calls cheese_and_crackers with the mathematical expression (10 + 20) passed to cheese_count and the mathematical expression (5 + 6) passed to boxes_of_crackers
cheese_and_crackers(10 + 20, 5 + 6)

# Prints the string
print "And we can combine the two, variables and math:"
# Calls cheese_and_crackers with the mathematical expression of (amount_of_cheese + 100) passed to cheese_count and the mathematical expression (amount_of_crackers + 1000) passed to boxes_of_crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
