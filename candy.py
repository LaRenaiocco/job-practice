# Can only eat 1/2 the candies.  How many types of candy can you have if you only eat 1/2?

def distributeCandies(candyType):
    """
    >>> distributeCandies([6,6,6,6])
    1
    >>> distributeCandies([1,1,2,3])
    2
    >>> distributeCandies([1,1,2,2,3,3])
    3
    """
    num_eaten = len(candyType) // 2
    num_types = len(set(candyType))
    if num_types <= num_eaten:
        return num_types
    else:
        return num_eaten
    
    # pseudocode:
    # need to know length of whole list / 2 is number of candies you can eat
    # make set of all candies so you know how many types you have
    # if len of set is less than or equal to 1/2 whole list
    # return len of set
    # else
    # return whole list / 2

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')