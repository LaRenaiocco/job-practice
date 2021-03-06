# CODEWARS 7kyu - SpoonerizeMe
# A spoonerism is a spoken phrase in which the first letters of two of the words 
# are swapped around, often with amusing results.

# In its most basic form a spoonerism is a two word phrase in which only the 
# first letters of each word are swapped:

# "not picking" --> "pot nicking"

# Your task is to create a function that takes a string of two words, separated
#  by a space: words and returns a spoonerism of those words in a string, as in 
#  the above example.

# NOTE: All input strings will contain only two words. Spoonerisms can be more 
# complex. For example, three-word phrases in which the first letters of the 
# first and last words are swapped: "pack of lies" --> "lack of pies" or more 
# than one letter from a word is swapped: "flat battery --> "bat flattery" 
# You are NOT expected to account for these, or any other nuances involved in 
# spoonerisms.

def spoonerize(words):
    """
    >>> spoonerize("nit picking")
    'pit nicking'
    >>> spoonerize("wedding bells")
    'bedding wells'
    >>> spoonerize("jelly beans")
    'belly jeans'
    """
    words_list = words.split(' ')
    return f'{words_list[1][0]}{words_list[0][1:]} {words_list[0][0]}{words_list[1][1:]}'


# pseudocode
# split words on space into a list of 2 words
# create variables to hold first letter of each word
# create result string with slices and first letters


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')