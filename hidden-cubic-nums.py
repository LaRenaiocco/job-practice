# codewars
# the instructions for this one are loooong
# https://www.codewars.com/kata/55031bba8cba40ada90011c4/train/python
# basic idea:
# parse numbers out of a string.  
# Numbers can be no longer than 3 digits
# if longer split apart into multiple digits
# check which digists are hidden cubes
# (ex 153 - 1**3 + 5**3 + 3**3 = 153)
# return string with all hidden cubes, plus sum total of cubes and 'Lucky'
# otherwise return 'Unlucky'

def is_sum_of_cubes(s):
    """
    # >>> is_sum_of_cubes("No numbers!")
    # 'Unlucky'
    # >>> is_sum_of_cubes("&z _upon 407298a --- ???ry, ww/100 I thought, 631str*ng and w===y -721&()")
    # '407 407 Lucky'
    # >>> is_sum_of_cubes(s = "aqdf& 0 1 xyz 153 777.777")
    # '0 1 153 154 Lucky'
    >>> is_sum_of_cubes("&z371 upon 407298a --- dreary, ###100.153 I thought, 9926315strong and weary -127&() 1") 
    '371 407 153 1 932 Lucky'
    """

    # will hold all 3 digit numbers in str form
    nums_list = []
    # create number variable
    num = ""

    for char in s:
        # try to convert to int and add string of int to num variable
        try:
            int(char)
            num += str(char)
        #  handles non int characters
        except:
            # if num varaible already has numbers in it, we need to assess
            # length and break into 3 digit numbers if too long
            if num != "":
                if len(num) > 3:
                    nums_to_add = split_long_num(num)
                    nums_list.extend(nums_to_add)
                    # print(nums_list)
                else:
                    nums_list.append(num)
                num = ""

    if num != "":
        if len(num) < 4:
            nums_list.append(num)
        else:
            nums_to_add = split_long_num(num)
            nums_list.extend(nums_to_add)

    # check if each num in nums list is a cube number
    cube_nums_list = check_hidden_cubes(nums_list)
    # find and return proper result
    if len(cube_nums_list) > 0:
        return prepare_result_string(cube_nums_list)
    else:
        return "Unlucky"
    


def split_long_num(num): #num input as string
    short_nums_list = []
    while len(num) > 3:
        short_num = num[0:3]
        short_nums_list.append(short_num)
        num = num[3:]
    short_nums_list.append(num)
    return short_nums_list

def check_hidden_cubes(nums_list): #nums_list holds nums in str form
    cube_nums_list = []
    for num in nums_list:
        total = 0
        for char in num:
            total += (int(char)**3)

        if total == int(num):
            cube_nums_list.append(total)
    return cube_nums_list


def prepare_result_string(cube_nums_list):
    result = ""
    cube_total = sum(cube_nums_list)
    for num in cube_nums_list:
        result += str(num) + " "
    return result + f'{cube_total} Lucky'


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')