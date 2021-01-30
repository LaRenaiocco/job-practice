#CodeWars 6kyu
# Break CamelCase
# Given a string in camelCase return a string with words broken apart

def solution(s):
    """
    >>> solution('breakCamelCase')
    'break Camel Case'
    >>> solution('canYouBreakApartThisSentence?')
    'can You Break Apart This Sentence?'
    """
    pass



# pseuodocode:
# check if each letter is uppercase.
# if letter is upper then we split string
# enumerate with index and char
# if letter is uppper
# track where uppercase index is
# create slice from previous track point to current index
# when we get to the end, create one last slice from previous track point to end
# append these slices to a string with a space

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')