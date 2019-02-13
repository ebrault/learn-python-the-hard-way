# Define name, set to "Emmet Brault"
name = "Emmet Brault"
# Define age, set to 27
age = 27
# Define height, set to 65
height = 65 # inches
# Define weight, set to 130
weight = 130 # lbs
# Define eyes, set to 'Brown'
eyes = 'Brown'
# Define teeth, set to 'White'
teeth = 'White'
# Define hair, set to 'Brown'
hair = 'Brown'

# Prints "Let's talk about Emmet Brault." using the string formatter and inserting the name variable
print "Let's talk about %s." % name
# Prints "He is 65 inches tall." using the decimal formatter and inserting the height variable
print "He is %d inches tall." % height
# Prints "He is 130 pounds heavy." using the decimal formatter and inserting the weight variable
print "He is %d pounds heavy." % weight
# Prints the string
print "Actually, that's not too heavy."
# Prints the string using the string formatter and inserting eyes and hair respectively delimited by parentheses and comma
print "He's got %s eyes and %s hair." % (eyes, hair)
# Prints the string using the string formatter and inserting the teeth variable
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it right
# Prints the string using the decimal formatter and inserting age, height, weight, and the sum respectively delimited by parentheses and commas
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
