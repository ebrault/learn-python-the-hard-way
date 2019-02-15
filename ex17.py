# Import argv module from sys
from sys import argv
# Import exists module from os.path
from os.path import exists

# Sets argv to script, from_file, to_file, i.e. the script
# the from_file, and the to_file need to be passed in for interpretation
script, from_file, to_file = argv

# Prints the string with the string formatters and inserts from_file and
# to_file
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too
# Sets in_file to open called on from_file
in_file = open(from_file)
# Sets indata to read called on in_file
indata = in_file.read()

# Prints the string with the decimal formatter and inserts len called on
# in data
print "The input file is %d bytes long" % len(indata)

# Prints the string with the raw data formatter and inserts exists called on
# to_file (to check if the file exists) to be inserted
print "Does the output file exist? %r" % exists(to_file)
# Prints the string
print "Ready, hit RETURN to continue, CTRL-C (^C) to abort."
# Allow for user input (i.e. RETURN or CTRL-C)
raw_input()

# Defines out_file as open called on to_file with write option
out_file = open(to_file, 'w')
# Calls write with indata passed as an argument on out_file, i.e. writes
# the value of indata to out_file
out_file.write(indata)

# Prints string
print "Alright, all done."

# Calls close on out_file
out_file.close()
# Calls close on in_file
in_file.close()
