# CODEWARS - 8kyu - Reduce but Grow
# Given a non-empty array of integers, return the result of multiplying the 
# values together in order.


def grow(arr):
    """
    >>> grow([1,2,3,4])
    24
    """
    result = 1
    for num in arr:
        result *= num
    return result

# pseudocode:
# create result variable set to 1
# loop through array
# for each number in array
# multiply result by number
# return result


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')