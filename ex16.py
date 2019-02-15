# Imports argv module from sys
from sys import argv

# Sets argv to script and filename (i.e. these must be passed when the script is run)
script, filename = argv

# Prints the string with the raw data fromatter and filename taken from argv inserted
print "We're going to erase %r." % filename
# Prints the string
print "If you don't wnat that hit CTRL-C (^C)."
# Prints the string
print "If you do want that, hit RETURN."

# Calls raw input with "?" passed as a parameter, allowing the user to choose between CTRL-C and RETURN
raw_input("?")

# Prints the string
print "Opening the file..."
# Sets target to open called on filename with the write option passed as a parameter
target = open(filename, 'w')

# Prints the string
print "Truncating the file. Goodbye!"
# Calls truncate on target
target.truncate()

# Prints the string
print "Now I'm going to ask you for three lines."

# Sets line1, line2, line3 to raw_input with the string passed allowing the user to input three lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Prints the string
print "I'm going to write these lines to the file."

# Calls write on target (i.e. open(filename)) and passes these six arguments
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Prints the string
print "And finally, we close it."
# Calls close on target
target.close()
