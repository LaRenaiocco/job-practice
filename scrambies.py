#CODEWARS 5kyu - Scarmblies
# Complete the function scramble(str1, str2) that returns true 
# if a portion of str1 characters can be rearranged to match str2, 
# otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). 
# No punctuation or digits will be included.
# Performance needs to be considered

# Attempt 1
# This version finds the correct answers but fails runtime!
def scramble(s1, s2):
    dict1 = {}
    for char in s1:
        dict1[char] = dict1.get(char, 0) + 1
    for char in s2:
        value = dict1.get(char)
        if value == None or value < 1:
            return False
        else:
            dict1[char] = value - 1
    return True

#pseudocode
#     create dictionary of string 1 letters with count as value
#     loop through string 2
#     if letter in string 2, in list 1
#     lower value by 1
#     if letter not in dict 1 or value is 0
#     return false
#     else, return true

#Attempt 3 - yaaaaay - this one passes the runtime!
def scramble(s1, s2):
    dict2 = {}
    for char in s2:
        dict2[char] = dict2.get(char, 0) + 1
    for char in s1:
        value = dict2.get(char)
        if value != None and value > 0:
            dict2[char] = value -1
    values = dict2.values()
    for item in values:
        if item != 0:
            return False
    return True

#Attempt 2
#also fails runtime
def scramble2(s1, s2):
    dict1 = {}
    dict2 = {}
    for char in s1:
        dict1[char] = dict1.get(char, 0) + 1
    for char in s2:
        dict2[char] = dict2.get(char, 0) + 1
    for key in dict2:
        value = dict2[key]
        compared_val = dict1.get(key)
        if compared_val == None or value > compared_val:
            return False
    return True

# pseudocode  
# create dictionaries of both strings
# check dictionary values in dict2 are less or equal to values in 1