# Split Strings - Codewars 6kyu
# Complete the solution so that it splits the string into pairs 
# of two characters. If the string contains an odd number of 
# characters then it should replace the missing second 
# character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

# takes in string of undetermined length. returns a list of 
# strings of length 2.  If og string is an odd length, final string
# should be char + _

def split_string(s): 
    """
    >>> split_string('abc')
    ['ab', 'c_']

    >>> split_string('abcdef')
    ['ab', 'cd', 'ef']
    """

    result = []
    for index, char in enumerate(s):
        if index % 2 == 0:
            new_string = char
            try:
                second_char = s[index + 1]
                new_string = new_string + second_char
            except:
                new_string = new_string + '_'
            result.append(new_string)

    return result

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')

# pseudocode:
# create a result list
# iterate through string
# if index is even, 
# create a string variable
# add character to string
# try index plus one:
# add to string variable
# Except
# add _ to string variable
# append string varaiable to result list