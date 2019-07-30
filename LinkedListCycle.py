# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(head == None or head.next == None or head.next.next == None):
            return False
        else:
            slow_ptr = head
            fast_ptr = head.next
            while(fast_ptr and fast_ptr.next):
                
                
                if(slow_ptr == fast_ptr):
                    return True
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            return False
