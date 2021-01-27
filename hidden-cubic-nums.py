def is_sum_of_cubes(s):
    """
    >>> is_sum_of_cubes("No numbers!")
    "Unlucky"
    >>> is_sum_of_cubes("&z _upon 407298a --- ???ry, ww/100 I thought, 631str*ng and w===y -721&()")
    "407 407 Lucky"
    >>> is_sum_of_cubes(s = "aqdf& 0 1 xyz 153 777.777")
    "0 1 153 154 Lucky"
    """
    #pseudocode
    # create empty list for numbers found
    # empty list for cube numbers
    # result string varaible
    # split string into list on space
    # for each item in list:
    #     create number variable
    #     for each char in item
    #     try to convert to int
    #         if yes, add to number variable (in string form)
    #     except
    #         pass
    #     if string length greater than 3, split string into groups of 3 and
    #     add string form of number variable to new list
    # loop through numbers list.
    #     make result variable
    #     for each char in string
    #         convert to int and cube it and add to result
    #     compare result to int of item in list
    #     if equal, add to cube numbers list
        
    # sum cube numbers list and create result string from numbers in  list and sum

        