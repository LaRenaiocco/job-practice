# CODEWARS 7kyu - Switcheroo
# Given a string made up of letters a, b, and/or c, switch the position of 
# letters a and b (change a to b and vice versa). Leave any incidence of c 
# untouched.


def switcheroo(string):
    """
    >>> switcheroo('acb')
    'bca'
    >>> switcheroo('aabacbaa')
    'bbabcabb'
    """
    result = ''
    for char in string:
        if char == 'a':
            result += 'b'
        elif char == 'b':
            result += 'a'
        else:
            result += 'c'
    return result

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')