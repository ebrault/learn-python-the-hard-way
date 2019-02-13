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

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
