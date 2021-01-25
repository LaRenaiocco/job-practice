# CODEWARS

def next_id(arr):
    """
    >>> next_id([0,1,2,3,4,5,6,7,8,9,10])
    11
    >>> next_id([5,4,3,2,1])
    0
    >>> next_id([0,1,2,3,5])
    4
    >>> next_id([])
    0
    """
    if arr == []:
        return 0
    arr_set = set(arr)
    sorted_arr = sorted(list(arr_set))
    if sorted_arr[0] != 0:
        return 0
    index = 0
    while index < len(sorted_arr) -1:
        if sorted_arr[index] + 1 != sorted_arr[index + 1]:
            return sorted_arr[index] + 1 
        else:
            index += 1
    return sorted_arr[-1] + 1

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')