# Import argv from sys
from sys import argv
# Import exists module from os.path
from os.path import exists

# Defines argv as script, from_file, to_file, i.e. the script,
# from_file, and to_file must be passed in when the script is interpreted
script, from_file, to_file = argv

# we could do these two on one line too
# Open from_file, copy contents
# Defines in_file as open called on from_file
in_file = open(from_file)
# Defines indata is read called on in_file
indata = in_file.read()

# Open to_file as writeable, paste contents
# Defines out_file as open called with to_file and write option passed
# as parameters
out_file = open(to_file, 'w')
# Calls write on out_file with indata passed, writes contents to out_file
out_file.write(indata)

# Prints the string
print "Alright, all done."

# Closes out_file
out_file.close()
# Closes in_file
in_file.close()
