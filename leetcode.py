# Assign Cookies #455
    def findContentChildren(g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        g.sort()
        s.sort()
        if len(s) == 0 or len(g) == 0:
            return 0
        while len(g) > 0 and len(s) > 0:
            if g[-1] <= s[-1]:
                count += 1
                g.pop()
                s.pop()
            elif g[-1] > s[-1]:
                g.pop()
        return count

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