#LeetCode
# Check If Two String Arrays are Equivalent

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word1_result = ""
        word2_result = ""
        for item in word1:
            word1_result += item
        for item in word2:
            word2_result += item
            
        if word1_result == word2_result:
            return True
        else:
            return False