# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if(head == None):
            return head
        
        temp = head
        
        while( head and (temp)):
            if(head.val == val):
                head = head.next
                temp = head
            else:
                if(temp.val != val):
                    prev = temp
                else:
                    prev.next = temp.next
            
                temp = temp.next
            head = head
        return head
