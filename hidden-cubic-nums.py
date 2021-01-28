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
    nums_list = []
    # empty list for cube numbers
    cube_nums_list = []
    # result string varaible
    result = ""
    # split string into list on space
    s_items = s.split(" ")
    print(s_items)
    # for each item in list:
    for item in s_items:
        # create number variable
        num = ""
        # for each char in item
        for char in item:
            # try to convert to int
            try:
                char_num = int(char)
                num += char
                # if len(num) == 3:
                #     print(f'try statement {num}')
                #     nums_list.append(num)
                #     num = ""
                
    #         if yes, add to number variable (in string form)
    #     except
            except:
                print(f'except statement {char}')
                if num != "":
                    print(f'except if statment {num}')
                    nums_list.append(num)
                    num = ""
    #         pass
        if len(num) > 0:
            nums_list.append(num)
        # if 0 < len(num) <= 3:
        #     nums_list.append(num)
        # while len(num) > 3:
        #     new_num = num[0:3]
        #     nums_list.append(new_num)
        #     num = num[3:]
        #     print(f'new num: {new_num}, num: {num}')
        print(nums_list)
    for index, num in enumerate(nums_list):
        while len(num) > 3:
            short_num = num[0:3]
            print(short_num)
            nums_list.append(short_num)
            num = num[3:]
            print(num)
    print(nums_list)


    #     if string length greater than 3, split string into groups of 3 and
    #     add string form of number variable to new list
    # loop through numbers list.
    #     make result variable
    #     for each char in string
    #         convert to int and cube it and add to result
    #     compare result to int of item in list
    #     if equal, add to cube numbers list
        
    # sum cube numbers list and create result string from numbers in  list and sum

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')