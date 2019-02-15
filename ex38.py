# Initializes ten_things and sets it to this string
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# Prints this string
print "Wait there's not 10 things in that list, let's fix that."

# Initializes stuff and sets it to ten_things split at ' ' (space)
stuff = ten_things.split(' ')
# Initializes more_stuff to the list of strings
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# While the length of stuff(ten_things.split(' ')) is not 10, i.e. stop when
# the length of stuff is 10
while len(stuff) != 10:
    # Initializes next_one to the first item popped off more_stuff
    next_one = more_stuff.pop()
    # Prints this string concatenated with the value of next_one
    print "Adding: ", next_one
    # Adds next_one to stuff (ten_things.split(' '))
    stuff.append(next_one)
    # Prints the string with the decimal formatter and inserts the length of
    # stuff at that point in the loop
    print "There's %d items now." % len(stuff)

# Prints the string concatenated with stuff
print "There we go: ", stuff

# Prints the string
print "Let's do some things with stuff."

# Prints the first element of stuff
print stuff[1]
# Prints the -1th element of stuff (last element)
print stuff[-1] # whoa! fancy
# Prints the first element removed
print stuff.pop()
# Prints stuff joined with a blank space
print ' '.join(stuff) # what? cool!
# Prints a slice of stuff from the third to the fifth elements joined with a #
print '#'.join(stuff[3:5]) # super stellar
