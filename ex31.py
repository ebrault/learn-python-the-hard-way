# Prints the string
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

# Initializes door and sets it to raw_input to set it to input from the user
door = raw_input("> ")

# First if branch.
# # If the user enters 1, print these three lines
if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    # Initializes bear and sets it to raw_input to set it to input from the user
    bear = raw_input("> ")

    # Second if branch
    # If the user enters 1, print this string
    if bear == "1":
        print "The bear eats your face off. Good job!"
    # Otherwise, if the user enters 2, print this string
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    # If the user enters any number other than 1 or 2, prints this string, with
    # the value of the input passed in
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

# First if branch. If the user enters 2, print these strings
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    # Initializes insanity to raw_input to set it to user input
    insanity = raw_input("> ")

    # Third if branch. If the user enters either 1 or 2, print this string
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    # If the user enters any number other than 1 or 2, print this string
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

# First if branch. If the user enters any number other than 1 or 2, print this string
else:
    print "You stumble around and fall on a knife and die. Good job!"
