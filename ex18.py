# this one is like your scripts with argv
# Defines a function print_two with the parameter (*args)
def print_two(*args):
    # Sets args to arg1 and arg2
    arg1, arg2 = args
    # Prints the string with the raw data formatter and arg1, arg2 inserted
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
# Defines print_two_again with parameters arg1 and arg2
def print_two_again(arg1, arg2):
    # Prints the string with the raw data formatter and arg1 and arg2 inserted
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
# Defines print_one with the parameter arg1
def print_one(arg1):
    # Prints the string with the raw data formatter and arg1 inserted
    print "arg1: %r" % arg1

# this one takes no arguments
# Defines print_none with no parameters
def print_none():
    # Prints the string
    print "I got nothin'."

# Calls print_two with the strings passed to *args
print_two("Emmet", "Brault")
# Calls print_two_again with the strings passed to arg1 and arg2
print_two_again("Emmet", "Brault")
# Calls print_one with the string passed to arg1
print_one("First!")
# Calls print none
print_none()
