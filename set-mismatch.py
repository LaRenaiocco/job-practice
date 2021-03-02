# LEETCODE Day 2
# You have a set of integers s, which originally contains all the numbers from 1 to n. 
# Unfortunately, due to some error, one of the numbers in s got duplicated to another 
# number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after 
# the error.

# Find the number that occurs twice and the number that is missing and return them 
# in the form of an array.

def set_mismatch(nums):
    """
    >>> set_mismatch([1, 2, 2, 4])
    [2, 3]
    >>> set_mismatch([1, 1])
    [1, 2]
    """
    # Handles if the length of the list is only 2
    if len(nums) == 2:
        if nums[0] == 1:
            return [1, 2]
        else:
            return [2, 1]
    nums.sort()
    # Handles if the missing number is the first or last number in the set
    if nums[0] != 1:
        missing = 1
    else: 
        missing = len(nums)
    # Loop to find where the errors in the list are
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            dupe = nums[i]
        elif nums[i] + 2 == nums[i + 1]:
            missing = nums[i] + 1
        i += 1
    return [dupe, missing]

# pseudocode:
# loop through list with an index variable, while less than length of list
# if next number is equal to, assign to a variable and pop from list
# if next number is equal to current num + 2, assign to a variable
# return array with first and second variable

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')