# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums_dict = {}
    for num in nums:
        nums_dict[num] = nums_dict.get(num, 0) + 1
    for key in nums_dict:
        if nums_dict[key] > 1:
            return True
    return False

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # make a dictionary where num is the key and a count of nums is the value
    # check dictionary for value that is 1, return key
    nums_dict = {}
    for num in nums:
        nums_dict[num] = nums_dict.get(num, 0) + 1
    return min(nums_dict, key=nums_dict.get)
        

# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

def balancedStringSplit(self, s):
    """
    :type s: str
    :rtype: int
    """
    balanced = 0
    count = 0
    for char in s:
        if char == "R":
            balanced += 1
        else:
            balanced -= 1
        if balanced == 0:
            count += 1
    return count

# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

def numberOfSteps (self, num):
    """
    :type num: int
    :rtype: int
    """
    # define a variable for result count
    result = 0
    # while num is not zero
    while num != 0:
        # if number is even
        if num % 2 == 0:
            # divide by 2
            num = num / 2
            # increase count by 1
            result += 1
        # if number is odd
        else:
            # subtract 1
            num -= 1
            # increase count by 1
            result += 1
    # return result count
    return result

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def moveZeroes(self, nums):
    """Moves all zeros in a list to end of list.  Alters in place."""
    # iterate through list and note index points of zeros in a new list
    index_of_zeros = []
    for index, num in enumerate(nums):
        if num == 0:
            index_of_zeros.append(index)
    # reverse new list.
    index_of_zeros = sorted(index_of_zeros, reverse=True)
    # note length of new list
    num_of_zeros = len(index_of_zeros)
    # pop out elements in list based on nums of new list
    for num in index_of_zeros:
        nums.pop(num)
    # append num of zeros to end of list that correspond to len of new list
    for num in range(num_of_zeros):
        nums.append(0)

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

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""
    pass
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