#Codewars 6kyu
# 1RM calculator
# there are 3 theories for calculating maximum weight 1RM based on 
# weight and repititions.  Which one has the highest weight?
# return integer rounded max weight
# If reps is 1, return weight
# if reps is 0, return 0

Epley
1RM = w(1 + (r/30))
McGlothin
1RM = (100*w)/(101.3-(2.67123*r))
Lombardi
1RM = (w*r)**0.10

def calculate_1RM(w, r):
    """
    >>> calculate_1RM(135,20)
    282
    >>> calculate_1RM(200,8)
    253
    >>> calculate_1RM(270,2)
    289
    >>> calculate_1RM(360,1)
    360
    >>>ncalculate_1RM(400,0)
    0
    """
    pass


# pseudocode:
#     if r = 0, return 0
#     if r = 1, return w
#     else:
#         solve all three ways and set to variable
#         check which variable is largest
#         return largest

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')