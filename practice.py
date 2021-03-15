#return a list of just the items between the duplicate items in list (codewars)
#Not at all pretty, but it works.
def duplicate_sandwich(arr):
    count_dict = {}
    for item in arr:
        count_dict[item] = count_dict.get(item, 0) + 1
    for key, value in count_dict.items():
        if value == 2:
            dup = key
    dup_index = []
    for index, item in enumerate(arr):
        if item == dup:
            dup_index.append(index)
    result = []
    for index, item in enumerate(arr):
        if index in range(dup_index[0] + 1, dup_index[1]):
            result.append(item)
    return result

#given an array and a number, find index at num and return num in array 
#to power of num.  If index doesn't exist, return -1

def index(array, n):
    try:
        return array[n] ** n
    except:
        return -1

# return sum of only nums in array that appear once (codewars)
def repeats(arr):
    single_nums = set([])
    for num in arr:
        if num not in single_nums:
            single_nums.add(num)
        else:
            single_nums.remove(num)
    return sum(single_nums)

#return the index of the number that is the least larger than number at 
#provided index (codewars)
def least_larger(a, i): 
#     set variable for number at index
    num_to_compare = a[i]
#     set variable for least larger list
    larger_nums = []
#     iterate through list checking if num is larger
    for num in a:
        if num > num_to_compare:
#     if it is add to list.
            larger_nums.append(num)
    if larger_nums == []:
        return -1
    else:
        least_larger = min(larger_nums)
#     return min of list
    for index, num in enumerate(a):
        if num == least_larger:
            return index


#  find the number of pairs of integers in array
def sockMerchant(n, ar):
    socks = {}
    pairs = 0
    for sock in ar:
        socks[sock] = socks.get(sock, 0) + 1
    for value in socks.values():
        pairs +=(value // 2)
    return pairs


def decode(s):
    """Decode a string.
    >>> decode("0h")
    'h'
    >>> decode("2abh")
    'h'
    >>> decode("0h1ae2bcy")
    'hey'
    """
    nums_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    result = ""
    for index, char in enumerate(s):
        if char in nums_set:
            skip = index + int(char) + 1
            result += s[skip]
    return result


# Check if a phrase has balanced parentheses
def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?
    >>> has_balanced_parens("()")
    True
    >>> has_balanced_parens("(Oh Noes!)(")
    False
    >>> has_balanced_parens("((There's a bonus open paren here.)")
    False
    >>> has_balanced_parens(")")
    False
    >>> has_balanced_parens("(")
    False
    >>> has_balanced_parens("(This has (too many closes.) ) )")
    False
    >>> has_balanced_parens("Hey...there are no parens here!")
    True
    """
    paren_count = 0
    for char in phrase:
        if char == "(":
            paren_count += 1
        if char == ")":
            paren_count -= 1
    if paren_count == 0:
        return True
    else:
        return False


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

# If one flower has even petals and one has odd, return True, else return False
#CodeWars
def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    else:
        return False

# CODEWARS Over the Road

def over_the_road(address, n):
    return n * 2 + 1 - address

# Mock Interview with Norris
# # Input: tokenizer('(add 2 (subtract 4 2))')
#   
# # Output:
# # [
# #     { 'type': 'paren', 'value': '(' },
# #     { 'type': 'name', 'value': 'add' },
# #     { 'type': 'number', 'value': '2' },
# #     { 'type': 'paren', 'value': '(' },
# #     { 'type': 'name', 'value': 'subtract' },
# #     { 'type': 'number', 'value': '4' },
# #     { 'type': 'number', 'value': '2' },
# #     { 'type': 'paren', 'value': ')' },
# #     { 'type': 'paren', 'value': ')' }
# # ]
# 
# create a variable to hold a word, start as empty string
# create a variable to hold a number in string form, strt as empty 
# results variable that is an empty list
# iterate through the string
# check if the item is a digit
#     add it to number varaible
# elif check if item is a paren
#     create the dictionary for the paren
#     append to the results
# elif if the item is a letter (isalpha)
#     append that letter to word variable
# elif if the item is a space
#     check if word variable had a word in it
#     if it does, create a dictionary item for the word
#     append to the results
#     clear the variable to empty string

# # Input: tokenizer('(add 2 'apple' (subtract 4 2))')

def tokenizer(string):
    
    word = ""
    number = ""
    results = []
    for char in string:
        if char.isdigit():
            number += char
        elif char ==  "(" or char ==  ")":
            if word != "":
                dict_item = {"type": "name", "value": word}
                results.append(dict_item)
                word = ""
            elif number != "":
                dict_item = {"type": "number", "value": number}
                results.append(dict_item)
                number = ""
            dict_item = {"type": "paren", "value": char}
            results.append(dict_item)
            
        elif char.isalpha():
            word += char
        else:
            if word != "":
                dict_item = {"type": "name", "value": word}
                results.append(dict_item)
                word = ""
            elif number != "":
                dict_item = {"type": "number", "value": number}
                results.append(dict_item)
                number = ""
    return results

# CODEWARS 7kyu Holiday III - Fire on a Boat
def fire_fight(s):
    boat_list = s.split()
    for index, item in enumerate(boat_list):
        if item == "Fire":
            boat_list[index] = "~~"
    return " ".join(boat_list)



# Split apart the string into a list on spaces
# loop through the list
# check if item in list is equal to "Fire"
# if yes, then replace fire with "~~"
# after looping through whole list
# join the list items back together into a string with spaces  


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')