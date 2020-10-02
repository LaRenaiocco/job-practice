def word_lengths(sentence):
    """Given a phrase, return dictionary keyed by word-length, 
    with the value for each length being the set of words of that length.
    Get dictionary of word-length: {words}.
    """
    word_list = sentence.split()
    result = {}
    for word in word_list:
        length = len(word)
        result[length] = result.get(length, set())
        result[length].add(word)
    return result


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).
    >>> lucky_numbers(0)
    []
    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    from random import randint
    result = []
    while len(result) < n:
        random_num = randint(1, 10)
        if random_num not in result:
            result.append(random_num)
    return result

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

