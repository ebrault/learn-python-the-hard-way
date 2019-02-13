# Defines formatter and assigns it the string of four raw input formatters
formatter = "%r %r %r %r"

# Prints formatter with 1, 2, 3, 4 inserted in as the values
print formatter % (1, 2, 3, 4)
# Prints formatter with strings "one" "two" "three" "four" inserted in as the values
print formatter % ("one", "two", "three", "four")
# Prints formatter with True False False True inserted in as the values
print formatter % (True, False, False, True)
# Prints formatter with the value of formatter ("%r %r %r %r") inserted in as the values
print formatter % (formatter, formatter, formatter, formatter)
# Prints formatter with the four string inserted in as the values
print formatter % (
    "I had this thing.",
    "That you could type right up.",
    "But it didn't sing.",
    "So I said goodnight."
)
