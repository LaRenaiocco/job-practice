# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space 
# complexity and O(n) runtime complexity?

# def missing_num(nums):
#     """
#     >>> missing_num([3,0,1])
#     2
#     >>> missing_num([0,1])
#     2
#     >>> missing_num([9,6,4,2,3,5,7,0,1])
#     8
#     >>> missing_num([0])
#     1
#     >>> missing_num([1, 2])
#     0
#     >>> missing_num([1])
#     0
#     """
#     if len(nums) == 1:
#         if nums[0] == 0:
#             return 1
#         else:
#             return 0
#     nums.sort()
#     if nums[0] != 0:
#         return 0
#     i = 0
#     while i < len(nums) - 1:
#         if nums[i] + 1 != nums[i + 1]:
#             return nums[i] + 1
#         i += 1
#     return nums[-1] + 1

    # pseudocode:
    # if length of list is 1, return 1
    # sort list
    # index variable
    # loop through list, to second to last spot 
    # compare number to next number, if not + 1, return current num + 1
    # after loop return nums[-1] + 1

def missing_num(nums):
    """
    >>> missing_num([3,0,1])
    2
    >>> missing_num([0,1])
    2
    >>> missing_num([9,6,4,2,3,5,7,0,1])
    8
    >>> missing_num([0])
    1
    >>> missing_num([1, 2])
    0
    >>> missing_num([1])
    0
    """
    n = len(nums) + 1
    total = sum(nums)
    max_total = 0
    for num in range(0, n):
        max_total += num
    return max_total - total

    # another idea:
    # check length of list.  max num should be len + 1
    # get sum of list
    # get sum of range of 0 to max num
    # subtract sum of list from max sum. 
    # result should be missing num.

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')