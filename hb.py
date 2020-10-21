# Decode a String
def decode(s):
    """
    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'
    >>> decode("0h1ae2bcy")
    'hey'
    """

    # iterate through String
    # if string can be made into an int - do it.
    # then add int + 1 and add that index spot to final string
    result = ""
    for index, char in enumerate(s):
        try:
            num = int(char)
            result += s[index + num + 1]
        except:
            pass

    return result



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')