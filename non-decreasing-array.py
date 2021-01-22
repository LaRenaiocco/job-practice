# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one element.

# Example 3:
# Input: [3,4,2,3]
# Output: false

def non_decreasing_array(nums):
    """
    >>> non_decreasing_array([4,2,3])
    True

    >>> non_decreasing_array([4,2,1])
    False

    >>> non_decreasing_array([3,4,2,3])
    False
    """
    count = 0
    for i in range(0, len(nums) -1):
        print(i)
        if nums[i] > nums[i +1]:
            count += 1
    if count > 1:
        return False
    else: 
        return True

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')