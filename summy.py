#CODEWARS 7ku
#Takes in string of numbers seperated by space
#return sum of numbers

def summy(string_of_ints):
    int_list = string_of_ints.split(" ")
    result = 0
    for i in int_list:
        result += int(i)
    return result

#pseudocode
# split string on spaces
# sum variable
# loop through list, for each
# convert to int and add to sum
# return sum