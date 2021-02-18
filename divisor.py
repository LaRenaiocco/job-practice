# 29. Divide Two Integers  -  LEETCODE
# Medium

# Add to List

# Share
# Given two integers dividend and divisor, divide two integers without using 
# multiplication, division, and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero, which means losing its 
# fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

# Note:

# Assume we are dealing with an environment that could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, 
# assume that your function returns 231 − 1 when the division result overflows.
 
def divide(dividend, divisor):
    """
    >>> divide(10, 3)
    3
    >>> divide(7, -3)
    -2
    >>> divide(0, 1)
    0
    >>> divide(1, 1)
    1
    """
    count = 0
    total = dividend
    if divisor < 0:
        while total >= (0 + divisor):
            count += 1
            total += divisor
    elif divisor > 0:
        while total >= (0 - divisor):
            count += 1
            total -= divisor
    else:
        return 0
    
    return count

# pseudocode
# count variable
# total variable
# if divisor is negative: 
#     while total is greater than 0 + divisor
#     count + 1
#     total = dividend +  divisor
# if divisor is positive:
#     while total is greater than 0 - divisor
#     count + 1
#     total = divident - divisor
# else 
#     return 0

# return count






if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')