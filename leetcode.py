#258: Add digits

def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    while num > 9:
        num = str(num)
        nums = []
        for char in num:
            nums.append(int(char))
        num = sum(nums)
    return num