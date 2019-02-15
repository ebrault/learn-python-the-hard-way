# Import argv module from sys
from sys import argv

# Set argv (i.e., argument variables to be passed in at execution) to script and filename
script, filename = argv

# Set txt to the open function called on filename passed in
txt = open(filename)

# Prints the string with the raw data formatter and filename inserted in
print "Here's your file %r:" % filename

# Prints read function called on txt (open(filename))
print txt.read()
# Calls close on txt (open(filename))
txt.close()

# Prints the string
print "Type the filename again:"
# Sets file_again as raw_input("> ") or whatever is entered into the console after the carrot
file_again = raw_input("> ")

# Sets txt_again to open called on whatever is passed to file_again
txt_again = open(file_again)

# Prints read called on txt_again
print txt_again.read()
# Calls close on txt_again
txt_again.close()
