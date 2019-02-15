# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
# Access element using bracket notation
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
# Access values with bracket notation on the key
# Print the string concatenated with the value at the key passed
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some states
print '-' * 10
# Access values with bracket notation on the key
# Prints the string concatenated with the value at the key passed
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
# Access values with bracketn otation on keys (can be nested)
# Prints the string concatenated with teh value at the key passed
# I.e., "Michigan has:, " cities[states['Michigan']] == "Detroit"
# == states['Michigan'] = 'MI, 'cities['MI'] = 'Detroit'
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
# Loop through objects, call items() on states to do so on states
for state, abbrev in states.items():
    # Print the string with the string formatters and the state and abbreviation
    # inserted
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
# Loop through objects, call items() on cities to do so on cities
for abbrev, city in cities.items():
    # Print the string with the string formatters and the abbreviation and city
    # Inserted
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
# Loop through objects, call items() on states to do so on states
for state, abbrev in states.items():
    # Print the string with string formatters and the string inserted
    print "%s state is abbreviated %s and has city %s" % (
    state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not exist
# Initialize state as .get called on states with 'Texas' and None passed in as
# arguments for key/value pair
state = states.get('Texas', None)

# If the state does not exist
if not state:
    # Print the string
    print "Sorry, no Texas."

# get a city with a default value
# Initialize city as .get called on cities with 'Texas', and 'Does not exist'
# Passed in as arguments for key/value pair
city = cities.get('TX', 'Does Not Exist')
# Prints the string with the string formatter and inserts the value of city
print "The city for the state 'TX' is: %s" % city
