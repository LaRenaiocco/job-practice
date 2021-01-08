#Leet Code
#Remove Duplicate values from a linked list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # assign head to current
        current = head
        # while current and current.next is not none do some things
        while current and current.next:
            # check if current.val and next.val are the same
            if current.val == current.next.val:
                # if yes, check for next next
                if current.next.next:
                    # if yes assign current.next to next next
                    current.next = current.next.next
                # if no reassign current to current.next
                else:
                    current.next = None
            # if values not equal, reassign current to move forward
            else:
                current = current.next
        #return head
        return head
        