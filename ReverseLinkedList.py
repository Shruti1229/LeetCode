# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head 
        while(current): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        head = prev 
        return head
