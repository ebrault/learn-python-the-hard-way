# Define constructor Other
class Other(object):

    # Define other.override()
    def override(self):
        # Prints string
        print "OTHER override()"

    # Define other.implicit()
    def implicit(self):
        # Prints string
        print "OTHER implicit()"

    # Define other.altered()
    def altered(self):
        # Prints string
        print "OTHER altered()"

# Defines Child constructor
class Child(object):
    # Child inherits from Other
    def __init__(self):
        self.other = Other()

    # child.implicit() calls other.implicit
    def implicit(self):
        self.other.implicit()

    # child.override()
    def override(self):
        # prints string
        print "CHILD override()"

    # child.altered()
    def altered(self):
        # prints string
        print "CHILD, BEFORE OTHER altered()"
        # child.altered = call to other.altered
        self.other.altered()
        # prints string
        print "CHILD, AFTER OTHER altered()"

# Initializes son as new Child
son = Child()

# calls child.implicit() on son, i.e. other.implicit()
son.implicit()
# Calls child.override() on son, i.e. child.override()
son.override()
# Calls child.altered(), i.e. prints string, calls other.altered()
# prints string
son.altered()
