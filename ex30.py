# Initializes people set to 69
people = 69
# Initializes cars set to 70
cars = 70
# Initializes buses set to 71
buses = 71

# If cars > people (i.e., if cars > people evaluates to true)
if cars > people:
    # Print the string
    print "We should take the cars."
# Otherwise (if cars > people evaluates to false), if cars < people (i.e., if cars < people evaluates to true)
elif cars < people:
    # Print the string
    print "We should not take cars."
# Otherwise, if cars < people evaluates to false and if cars > people evaluates to false
else:
    # Print the string
    print "We can't decide."

# Evaluates the statement buses > cars
if buses > cars:
    # If buses > cars evalutes to true, print the string
    print "That's too many buses."
# If buses > cars evalutes to false, evalute the statement buses < cars
elif buses < cars:
    # If buses < cars evaluates to true print the string
    print "Maybe we could take the buses."
# If neither buses > cars nor buses < cars evalutes to true
else:
    # Print the string
    print "We still can't decide."

# Evaluates the statement people > buses
if people > buses:
    # If the statement is true, print the string
    print "Alright, let's just take the buses."
# If people > buses evaluates to false
else:
    # Print the string
    print "Fine, let's stay home then."
