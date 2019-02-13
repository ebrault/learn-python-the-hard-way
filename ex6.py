# Defines x as this string and uses decimal formatter to insert the value
x = "There are %d types of people." % 10
# Defines binary as the string "binary"
binary = "binary"
# Defines do_not as "don't"
do_not = "don't"
# Defines y as this string and uses string formatters to insert the values of binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints x
print x
# Prints y
print y

# Prints "I said x" using the raw data formatter and inserting the value of x
print "I said: %r" % x
# Prints "I also said 'y'" using the string formatter and inserting the value of y
print "I also said '%s'." % y

# Defines hilarious and sets it to false
hilarious = False
# Defines joke_evaluation and sets it to "Isn't that joke so funny?! %r"
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints joke_evaluation with the value of hilarious inserted in for the raw data formatter
print joke_evaluation % hilarious

# Sets w to string
w = "This is the left side of..."
# Sets e to string
e = "a string with a right side"

# Concatenates two strings using + operator
print w + e
