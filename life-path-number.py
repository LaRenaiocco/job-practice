# Codewars 7kyu
# goal to use/practice recursion
# Given DOB in form of string "YYYY-MM-DD"
# return single digit number derived from adding all the numbers in birthdate

def life_path_number(birthdate):
    if len(birthdate) == 1:
        return int(birthdate)
    nums_list = []
    for char in birthdate:
        if char != "-":
            nums_list.append(int(char))
    birthdate = sum(nums_list)
    return life_path_number(str(birthdate))