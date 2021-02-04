    # Complete the function that takes two numbers as input, 
    # num and nth and return the nth digit of num 
    # (counting from right to left).

    # Note
    # If num is negative, ignore its sign and treat it as a positive value
    # If nth is not positive, return -1
    # Keep in mind that 42 = 00042. This means that findDigit(42, 5) 
    # would return 0

def findDigit(num,nth):
    """
    >>> findDigit(5673, 4)
    5
    >>> findDigit(129, 2)
    2
    >>> findDigit(-2825, 3)
    8
    >>> findDigit(-456, 4)
    0
    >>> findDigit(0, 20)
    0
    >>> findDigit(65, 0)
    -1
    >>> findDigit(24, -8)
    -1
    """

# pseudocode
# if nth is  ) or a negative num, return -1
# convert number to string
# if first char is "-" slice off -
# if length of number is less than nth, return 0
# return number[- nth] in int form

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
