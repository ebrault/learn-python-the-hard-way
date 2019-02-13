# Prints string
print "Mary had a little lamb."
# Prints string using string formatter to insert 'snow'
print "Its fleece was white as %s" % 'snow'
# Prints string
print "And everywhere that Mary went."
# Prints "." ten times on the same line
print "." * 10 # what'd that do?

# Defines variables end1 - end12 as the letters of "CheeseBurger"
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# Prints the first six letters, delimited by a comma
print end1 + end2 + end3 + end4 + end5 + end6,
# Prints the remaining six letters on the same line, because of the comma
print end7 + end8 + end9 + end10 + end11 + end12
