"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats:

>>> compress('aabbaabb')
'a2b2a2b2'

If a character appears once, it should not be followed by a number:

>>> compress('abc')
'abc'

The function should handle letters, whitespace, and punctuation:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""


def compress(string):
    """Return a compressed version of the given string."""
    char_list = []
    for char in string:
        char_list.append(char)
    new_list = [char_list[0]]
    index = 0
    count = 1
    while index < len(char_list)-1:
        if char_list[index] == char_list[index + 1]:
            count += 1
        else:
            if count != 1:
                new_list.append(str(count))
                count = 1
            new_list.append(char_list[index + 1])
        index += 1
    if count != 1:
        new_list.append(str(count))
    new_string = "".join(new_list)
    return new_string

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')

