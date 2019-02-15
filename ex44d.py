# Defines constructor Parent
class Parent(object):

    # Defines parent.override()
    def override(self):
        # Prints string when called
        print "PARENT override()"

    # Defines parent.implicit()
    def implicit(self):
        # Prints string when called
        print "PARENT implicit()"

    # Defines parent.altered()
    def altered(self):
        # Prints string when called
        print "PARENT altered()"

# Defines Child constructor that inherets from Parent
class Child(Parent):

    # Defines child.override()
    def override(self):
        # Prints string when called
        print "CHILD override()"

    # Defines child.altered()
    def altered(self):
        # Prints string when called
        print "CHILD, BEFORE PARENT altered()"
        # Calls super altered (i.e. child.altered = parent.altered())
        super(Child, self).altered()
        # Prints string
        print "CHILD, AFTER PARENT altered()"

# Initializes dad to new instance of Parent
dad = Parent()
# Initializes son to new instance of Child
son = Child()

# Calls parent.implicit()
dad.implicit()
# Calls child.implicit() == parent.implicit() (no child.implicit)
# defined but Child inherits parent.implicit implicitly
son.implicit()

# Calls parent.override()
dad.override()
# Calls child.override()
son.override()

# Calls parent.altered
dad.altered()
# Calls child.altered == call super to parent.altered()
son.altered()
