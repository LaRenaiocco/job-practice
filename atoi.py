# Leetcode medium
# Implement the myAtoi(string s) function, which converts a string 
# to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) 
# is '-' or '+'. Read this character in if it is either. This 
# determines if the final result is negative or positive respectively. 
# Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit charcter or 
# the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, 
# "0032" -> 32). If no digits were read, then the integer is 0. 
# Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range 
# [-2**31, 2**31 - 1], then clamp the integer so that it remains 
# in the range. Specifically, integers less than -231 should be 
# clamped to -2**31, and integers greater than 231 - 1 should be 
# clamped to 2**31 - 1.
# Return the integer as the final result.
# Note:

# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or 
# the rest of the string after the digits.

def myAtoi(s):
    pass

# concept:
# intake string, return integer
# string may have leading white space
# string may have a +. - or neither (if neither, integer should be +)
# string may have other characters after digits
# if number is greater than 2 ** 31 -1, should return 2 ** 31 -1
# if number is less than -2 ** 31, return  -2 ** 31

# pseudocode:
# remove whitespace with .strip()
# if string is now empty, return 0
# if string is not empty continue 
# check first char, if it is a +, remove it with slice
# if it is a -, remove with slice and set a negative variable to true
# loop through string with enumerate
# check if each char is a digit.
# if yes, pass,
# if no, create a slice from 0, to current char
# if negative set to true, return int of slice * -1
# else, return int of slice

# ____________Other Idea____________
# set empty variable for result
# check if first char in string is +, -, or a digit.
# if -, result will be negative, add a "-" to res
# if + or digit, result will be positive

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')