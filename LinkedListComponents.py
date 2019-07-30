# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        count = 0
        while head:
            if head.val in G and (head.next == None or head.next.val not in G):
                count += 1
            head = head.next
        return count
