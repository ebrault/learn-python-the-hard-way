# Defines constructor Parent
class Parent(object):

    # Defines function override taking parameter self (i.e., Parent)
    def override(self):
        # Prints string when called
        print "PARENT override()"

# Defines constructor Child which inherits from Parent
class Child(Parent):

    # Defines function override for Child taking parameter self (i.e. Child)
    # Overrides inheritance in this case (separate function)
    def override(self):
        # Prints string when called
        print "CHILD override()"

# Initializes dad as an instance of Parent
dad = Parent()
# Initializes son as an instance of Child
son = Child()

# Calls override on dad, i.e. prints "PARENT Override()"
dad.override()
# Calls override on son, i.e. prints "CHILD override()"
# This is an override
son.override()
