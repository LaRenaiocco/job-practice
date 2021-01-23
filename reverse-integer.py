#LEETCODE
# Given a signed 32-bit integer x, return x with its digits 
# reversed. If reversing x causes the value to go outside 
# the signed 32-bit integer range [-231, 231 - 1], then return 0.

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    string_x = str(x)
    result = ""
    list_x = []
    if x < 0:
        result += "-"
        string_x = string_x[1:]
    for char in string_x:
        list_x.append(char)
    while len(list_x) > 0:
        num = list_x.pop()
        result += num
    result = int(result)
    if ((-2**31) -1) > result  or result > ((2**31) -1):
        return 0
    return result
        
        #PSEUDOCODE
#         convert number to a string
#         create result string
#         first check if number is negative
#         if yes, 
#         result string starts with '-'
#         slice off - from variable
#         convert string to a list
#         while list length is greater than 0:
#             pop off last item of list and append to result string
            
#         convert result back to number and return
        
        