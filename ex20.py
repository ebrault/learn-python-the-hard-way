# Imports the argv package from the sys module
from sys import argv

# Define argument values to be passed when script is executed
script, input_file = argv

# Define function print_all to be passed parameter f
def print_all(f):
    # Calls .read() on file f, prints all lines of file
    print f.read()

# Define function rewind to be passed parameter f
def rewind(f):
    # Calls .seek() on f with 0 passed as an argument
    # seek(0) goes back to the start of file (byte 0)
    f.seek(0)

# Define function print_a_line to be passed line_count and f parameters
def print_a_line(line_count, f):
    # Prints the line that the script is on and calls readline() on f
    print line_count, f.readline()

# Defines current_file as open with input_file from argv passed
current_file = open(input_file)

# Prints string
print "First let's print the whole file:\n"

# Calls print_all with current_file (i.e., open(input_file)) passed as an argument
# Prints all lines of the file
print_all(current_file)

# Prints string
print "Now let's rewind, kind of like a tape."

# Calls rewind with current_file (i.e., open(input_file)) passed as an argument
# Effectively rewind(open(input_file)) or open(input_file).seek(0)
rewind(current_file)

# Prints string
print "Let's print three lines:"

# Defines current line as line 1
current_line = 1
# Calls print_a_line with current_line (line 1) and current_file (open(input_file)) passed as arguments
print_a_line(current_line, current_file)

# Redefines current_line as current_line (1) + 1, i.e., line 2
current_line += 1
# Calls print_a_line with current_line (line 2) and current_file (open(input_file)) passed as arguments
print_a_line(current_line, current_file)

# Redefines current_line as current_line (2) + 1, i.e. line 3
current_line += 1
# Calls print_a_line with current_line (line 3) and current_file (open(input_file)) passed as arguments
print_a_line(current_line, current_file)
