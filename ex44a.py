# Defines constructor Parent
class Parent(object):

    # Defines function implicit for Parent
    def implicit(self):
        # Prints string
        print "PARENT implicit()"

# Defines constructor Child that inherits from Parent
class Child(Parent):
    pass

# Initializes dad to an instance of parent
dad = Parent()
# Initializes son to an instance of child (which is an instance of parent)
son = Child()

# Calls implicit on dad, prints "PARENT implicit()"
dad.implicit()
# Calls implicit on son, prints "PARENT implicit()"
son.implicit()
