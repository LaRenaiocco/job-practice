# Story
# In the fictional country of Bugliem, you can ask for a custom licence 
# plate on your car, provided that it meets the followoing criteria:

# it's 2-8 characters long
# it contains only letters A-Z, numbers 0-9, and dashes -
# letters and numbers are separated by a dash
# it doesn't start or end with a dash, and it doesn't have consecutive dashes
# it's not made up of numbers only# You also have to pay 1000 local units to obtain one, although this will not be tested.

# Task
# To make the life of the local authorities easier 
# (and get your driving record cleaned), 
# you need to implement a function that accepts an ascii input string, 
# and returns the number plate if possible.

# You have to replace all special characters and spaces with dashes 
# (consecutive characters should be replaced with a single dash), 
# and truncate the result to maximum 8 characters (if longer). 
# If the result complies with the above criteria, 
# return it capitalized; otherwise return "not possible".

# Examples
# "mercedes"    -->  "MERCEDES"
# "anter69"     -->  "ANTER-69"
# "1st"         -->  "1-ST"
# "~c0d3w4rs~"  -->  "C-0-D-3"
# "I'm cool!"   -->  "I-M-COOL"
# "1337"        -->  "not possible"

def licence_plate(s):
    # your brilliant code here
    pass

# Task
# return plate with max of 8 characters or "not possible"
# cannot start or end with -
# not more than 1 dash in a row
# special chars replaced with dash
# dash between letters and numbers

# pseudocode:
# plate result variable
# variable for previous character tracking for easy comparison
# iterate through input, while result is less than 8
# if char is alpha
#     if length of result is 0:
#         append char as upper
#     check if previous is alpha
#         if yes, append char as uppercase
#         update previous
#     if previous is dash
#         append char as uppercase
#         update previous
#     if previous is numeric
#         append dash
#         append char as uppercase
#         update previous
# if char is numeric
#     if length of result is 0
#         append char
#         update previous
#     if previous is numeric
#         append char
#         update previous
#     if previous is alpha
#         append dash
#         append char
#         update previous
#     if previous is dashes
#         append char
#         update previous
#     else (assumes char is not alpha or numeric, must be special char)
#         if result lenght is 0:
#             pass
#         if legth is 7
#             return result
#         if previous is dash
#             pass 
#         else:
#             append a dash
#             update previous
# return slice of result from [0:8]




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')