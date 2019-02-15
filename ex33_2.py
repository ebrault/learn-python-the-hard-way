# Defines a function loop with the parameter num
def loop(num):
    # Initializes int i and sets it to 0
    i = 0
    # Initializes list numbers and sets it to empty list
    numbers = []
    # While i is less than num, i.e. loop until i = num
    while i < num:
        # Print string with the decimal formatter and the value of i
        # at the start of that moment in the loop inserted
        print "At the top i is %d" % i
        # Add i to the empty list of numbers
        numbers.append(i)

        # Reassign i to i+2
        i += 2
        # Print the string, concatenate the list
        print "Numbers now: ", numbers

        # Print the string with the decimal formatter and the value of i
        # at the end of that moment in the loop inserted
        print "At the bottom i is %d" %i

        # Print the string
        print "The numbers: "

        # Loop through numbers at that moment in the loop and print them individually
        for k in numbers:
            print k

# Call loop with 10 passed as the argument
loop(10)
