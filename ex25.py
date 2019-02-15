# Defines the function break_words with the parameter stuff
def break_words(stuff):
    # Describes what the function does
    """This function will break up words for us"""
    # Sets words to the split function with a space (' ') passed
    # as an argument
    words = stuff.split(' ')
    # Returns words
    return words

# Defines sort_words with the parameter words
def sort_words(words):
    # Describes what the function does
    """Sorts the words."""
    # Returns sorted called on words
    return sorted(words)

# Defines print_first_word with the parameter words
def print_first_word(words):
    # Describes what the function does
    """Prints the first word after popping it off."""
    # Sets word to words with pop(0) called on it, i.e. words with the 0th element removed
    word = words.pop(0)
    # Prints word
    print word

# Defines print_last_word with parameter words
def print_last_word(words):
    # Describes what the function does
    """Prints the last word after popping it off."""
    # Sets word to words with pop(-1) called on it, i.e. words with the -1th element removed
    word = words.pop(-1)
    # Prints word
    print word

# Defines sort_sentence with the parameter sentence
def sort_sentence(sentence):
    # Describes what the function does
    """Takes in a full sentence and returns the sorted words."""
    # Sets words to break_words called on sentence
    words = break_words(sentence)
    # returns sort_words called on words
    return sort_words(words)

# Defines print_first_and_last with the parameter sentence
def print_first_and_last(sentence):
    # Sets words to break_words called on sentence
    words = break_words(sentence)
    # Calls print_first_word on words
    print_first_word(words)
    # Calls print_last_word on words
    print_last_word(words)

# Defines print_first_and_last_sorted with the parameter sentence
def print_first_and_last_sorted(sentence):
    # Sets words to sort_sentence called on sentence
    words = sort_sentence(sentence)
    # Calls print_first_word on words
    print_first_word(words)
    # Calls print_last_word on words
    print_last_word(words)
