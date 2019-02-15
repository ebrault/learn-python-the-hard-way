# Defines the function add with the parameters a and b
def add(a, b):
    # Prints the string with the decimal formatters and inserts a and b
    print "ADDING %d + %d" % (a, b)
    # Returns the sum of a and b
    return a + b

# Defines the function subtract with the parameters a and b
def subtract(a, b):
    # Prints the string with decimal formatters and inserts a and b
    print "SUBTRACTING %d - %d" % (a, b)
    # Returns the difference of a and b
    return a - b

# Defines the function multiply with the parameters a and b
def multiply(a, b):
    # Prints the string with decimal formatters and inserts a and b
    print "MULTIPLYING %d * %d" % (a, b)
    # Returns the product of a and b
    return a * b

# Defines the function divide with the parameters a and b
def divide(a, b):
    # Prints the string with decimal formatters and inserts a and b
    print "DIVIDING %d / %d" % (a, b)
    # Returns the quotient of a and b
    return a / b

# Prints the string
print "Let's do some math with just functions!"

# Sets age to add called with arguments 30 and 5
age = add(30, 5)
# Sets height to subtract called with arguments 78 and 4
height = subtract(78, 4)
# Sets weight to multiply called with arguments 90 and 2
weight = multiply(90, 2)
# Sets iq to divide called with arguments 100 and 2
iq = divide(100, 2)

# Prints the string with decimal formatters and age, height, weight, and iq inserted
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for extra credit, type it in anyway.
# Prints the string
print "Here is a puzzle."

# Sets what to divide called on iq and 2, calls multiply on that value and weight
# calls subtract on that value and height, and calls add on that value and age
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# Prints the string, concatenates with what
print "That becomes: ", what, "Can you do it by hand?"

# By hand divide(iq, 2) = 25, multiply (180, 25) = 4500
# subtract (74, 4500) = -4426, add 35 + -4426 = -4391
