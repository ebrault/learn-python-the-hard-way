# Imports argument variables module from system
from sys import argv

# Defines argument variables as script and filename, to be passed when program is run
script, filename = argv

# Defines txt as the open method called on the argument variable "filename"
txt = open(filename)

# Prints the string using the raw data formatter with the value of filename inserted
print "Here's your file %r:" % filename
# Prints the .read() method called on txt with no arguments passed (i.e. reads until EOF)
print txt.read()
txt.close()

# Prints the string
print "Type the filename again:"
# Defines file_again as raw_input with the carrot allowing the user to type the filename again
file_again = raw_input("> ")

# Defines txt_again as the open method called on file_again (i.e., filename passed in to raw_input)
txt_again = open(file_again)

# Prints the .read() method called on txt_again with no arguments passed (i.e., reads the file passed in to txt_again until EOF)
print txt_again.read()
txt_again.close()
