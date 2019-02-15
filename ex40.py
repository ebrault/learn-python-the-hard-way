# Defines constructor class song that accepts an object as its parameters
class Song(object):

    # Called after the instance has been created and passed to the constructor
    # when it is created. Takes self, and lyrics as parameters. Creates the
    # variable lyrics for that particular instance of song
    def __init__(self, lyrics):
        # Sets the lyrics of song to lyrics passed in on construction
        self.lyrics = lyrics

    # Defines a function sing_me_a_song that will be called on the constructed
    # object
    def sing_me_a_song(self):
        # Iterates through the lines of the lyrics
        for line in self.lyrics:
            # Prints each line of the lyrics
            print line

# Initializes happy_bday as a new Song constructor with lyrics passed as a
# list
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

# Initializes bulls_on_parade as a new Song constructor with different lyrics
# Passed as a list
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells."])

# Calls sing_me_a_song on the constructed happy_bday object
happy_bday.sing_me_a_song()

# Calls sing_me_a_song on the constructed bulls_on_parade object
bulls_on_parade.sing_me_a_song()
