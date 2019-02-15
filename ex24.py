# Prints the string
print "Let's practice everything"
# Prints the string with escape sequences
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# Sets poem to multi-line string with escape sequences
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Prints 12 dashes
print "---------------"
# Prints poem
print poem
# Prints 12 dashes
print "---------------"

# Sets five to this computation (10 - 2) + (3 - 6) = 8 + -3 = 5
five = 10 - 2 + 3 - 6
# Prints the string with the string formatter and inserts the variable for above
# computation
print "This should be five: %s" % five

# Defines function secret formula with variable started as parameter
def secret_formula(started):
    # Sets jelly_beans to whatever argument is passed in to started * 500
    jelly_beans = started * 500
    # Sets jars to jelly_beans / 1000
    jars = jelly_beans / 1000
    # Sets crates to jars / 100
    crates = jars / 100
    # Returns the values of jelly_beans, jars, and crates
    return jelly_beans, jars, crates

# Sets start point to 10,000
start_point = 10000
# Calls secret_formula with start_point passed as argument to started
beans, jars, crates = secret_formula(start_point)
# Effectively
    # jelly_beans = 10,000 * 500
    # jars = jelly_beans / 1000 = 5,000,000 / 1000 = 5000
    # crates = jars / 100 = 50
    # return 5,000,000 , 5000, 50
# beans, jars, crates = 5,000,000, 5000, 50

# Prints string with decimal formatter and inserts start_point
print "With a starting point of: %d" % start_point
# Prints string with decimal formatters and inserts beans, jars, crats variables computed by calling secret_formula on start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# Reassigns start_point to start_point / 10
start_point = start_point / 10

# Prints string
print "We can also do that this way:"
# Prints string with decimal formatters inserting a function call of secret_formula on reassigned value of start_point
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
# Effectively
    # jelly_beans = 1000 * 500 = 500,000
    # jars = jelly_beans / 1000 = 500,000 / 1000 = 500
    # crates = jars / 100 = 500 / 100 = 5
    # Prints "We'd have 500000 beans, 500 jars, and 5 crates"
