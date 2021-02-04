# Given a string made of digits [0-9], return a string 
# where each digit is repeated a number of times equals to its value.

def explode(s):
    """
>>> explode("312")
'333122'
>>> explode("102269")
'12222666666999999999'
"""
    result = ""
    for char in s:
        result += char * int(char)
    return result
# pseudocode:
# create result varaible as empty string
# iterate through string
# for each number in string:
#     result += "char" * int(char)
# return result

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')