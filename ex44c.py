# Defines Parent constructor
class Parent(object):

    # Defines function altered accepting parameter self
    def altered(self):
        # Prints string when called
        print "PARENT altered()"

# Defines Child constructor which inherits from Parent
class Child(Parent):

    # Defines function altered accepting parameter self
    def altered(self):
        # Prints string when called
        print "CHILD, BEFORE PARENT altered()"
        # Calls super altered, i.e. altered of object it inherits from (parent.altered())
        super(Child, self).altered()
        # Prints string when called
        print "CHILD, AFTER PARENT altered()"

# Initializes dad as an instance of Parent
dad = Parent()
# Initializes son as an instance of Child
son = Child()

# Calls altered on dad, i.e. Parent.altered(), prints "PARENT altered()"
dad.altered()
# Calls altered on son, i.e. Child.altered() == Parent.altered(),
# Prints "CHILD BEFORE PARENT altered()", "PARENT altered()", "CHILD AFTER PARENT altered()"
# This is an override
son.altered()
