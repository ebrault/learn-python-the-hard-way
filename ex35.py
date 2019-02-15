# Import exit from sys allowing programs to be terminated on call to it
from sys import exit

# Define gold room as void function (no parameter)
def gold_room():
    # Print the string
    print "This room is full of gold. How much do you take?"

    # Initialize next and set it to raw_input to set it user input
    next = raw_input("> ")
    # First if branch in gold room. If user enters 1 or 0
    if "0" in next or "1" in next:
        # Set how much to cast input to an int
        how_much = int(next)
    # If the user enters anything other than 1 or 0, call dead
    # with the string passed as an argument
    else:
        dead("Man, learn how to type a number.")

    # Second if branch. If how_much is less than 50
    if how_much < 50:
        # Print this string
        print "Nice, you're not greedy, you win!"
        # Call exit with 0 passed to terminate the program
        exit(0)
    # Otherwise, call dead with this string passed
    else:
        dead("You greedy bastard!")

# Defines void function bear room
def bear_room():
    # Prints these strings
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    # Initializes bear_moved to False
    bear_moved = False

    # Infinite loop, never becomes false
    while True:
        # Initializes next and sets it to raw_input to set it to user input
        next = raw_input("> ")

        # First if branch in gold room. If the user enters "take honey"
        if next == "take honey":
            # Call dead with this string passed as an argument
            dead("The bear looks at you then slaps your face off.")
        # Otherwise, if the user enters taunt bear and bear_moved = True
        elif next == "taunt bear" and not bear_moved:
            # Print this string
            print "The bear has moved from the door. You can go through it now."
            # Set bear_moved to true
            bear_moved = True
        # Otherwise, if the user enters taunt bear and bear_moved = false
        elif next == "taunt bear" and bear_moved:
            # Call dead with this string passed as an argument
            dead("The bear gets pissed off and chews your leg off.")
        # Otherwise if the user enters open door and bear_moved = false
        elif next == "open door" and bear_moved:
            # Call gold_room and go through that process
            gold_room()
        # Otherwise if the user enters none of these options print this string
        else:
            print "I got no idea what that means."

# Define void function cthulhu_room
def cthulhu_room():
    # Print these strings
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    # Initialize next and set it to raw_input to set it to the user's input
    next = raw_input("> ")

    # First if branch in cthluhu_room, If the user enters flee
    if "flee" in next:
        # Call start
        start()
    # Otherwise, if the user enters "head"
    elif "head" in next:
        # Call dead with this string passed as an argument
        dead("Well that was tasty!")
    else:
        # Otherwise, if the user enters none of these options, recursively
        # call cthulhu room to start the process again
        cthulhu_room()

# Defines function dead, with parameter why
def dead(why):
    # Dead prints the string passed to why on function call concatenated with
    # Good job!
    print why, "Good job!"
    # Terminates the program
    exit(0)

# Defines void function start
def start():
    # Prints these strings
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    # Initialize next and set it to raw_input to set it to user input
    next = raw_input("> ")

    # First if branch in start. If the user enters left
    if next == "left":
        # Call bear_room
        bear_room()
    # Otherwise, if the user enters right
    elif next == "right":
        # Call cthulhu_room
        cthulhu_room()
    # Otherwise, if the user enters neither left nor right call dead with this
    # string passed as an argument
    else:
        dead("You stumble around the room until you starve.")

# Call start to start the program
start()
