# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

def subtractProductAndSum(self, n):
    """ Subtract sum from product of digits on an integer"""
    # convert integer to string and split into a list
    str_list = list(str(n))
    # create sum variable
    sumation = 0
    # create product variable
    product = 1
    # iterate through list
    for char in str_list:
        num = int(char)
        # convert each item to int and add to sum total
        sumation += num
        # convert each item to int and multiply to product total
        product *= num
    # return product minus sum
    return product - sumation

# Given an integer n, return a list containing n unique random numbers between 1-10, inclusive.

# def lucky_numbers(n):
#     """Return n unique random numbers from 1-10 (inclusive)."""

#     from random import randint

#     lucky_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     result = set([])
#     for num in range(1, n + 1):
#         lucky = randint(lucky_nums)
#         if lucky not in result:
#             result.append(lucky)
#         else

# Given two lists. concatenate them (that is, combine them into a single list).

def concat_lists(list1, list2):
    """Combine lists.
    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> concat_lists([], [1, 2])
    [1, 2]
    >>> concat_lists([1, 2], [])
    [1, 2]
    >>> concat_lists([], [])
    []
    """

    result = list1
    for item in list2:
        result.append(item)
    return result


# Given list of ints, return True if any two nums in list sum to 0.

def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0.
    >>> add_to_zero([])
    False
    >>> add_to_zero([1])
    False
    >>> add_to_zero([1, 2, 3])
    False
    >>> add_to_zero([1, 2, 3, -2])
    True
"""
    set_nums = set(nums)
    for num in set_nums:
        if -num in set_nums:
            return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()