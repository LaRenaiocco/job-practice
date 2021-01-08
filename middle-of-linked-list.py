#LEETCODE - Find middle of a linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result_list = []
        current = head
        while current:
            result_list.append(current)
            current = current.next
        return result_list[len(result_list) / 2]