# Initializes i and sets it to 0
i = 0
# Initializes numbers and sets it to an empty list
numbers = []

# While loop. Until i = 6
while i < 6:
    # Print the string with the decimal formatter and i inserted where
    # i is the value of i at the start of that moment in the loop
    print "At the top i is %d" % i
    # Add i at that moment to the list
    numbers.append(i)

    # Reassign i to i+1
    i += 1
    # Print the string concatenated with the list
    print "Numbers now: ", numbers

    # Print the string with the decimal formatter and i inserted where
    # i is the value of i at the end of that moment in the loop
    print "At the bottom i is %d" % i

# Print the string
print "The numbers: "

# Loop through the list of numbers and print them individually
for num in numbers:
    print num
