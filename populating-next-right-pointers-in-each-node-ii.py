"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import defaultdict
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        graph = defaultdict(list)
        dep = 0
        
        stack = []
        if root:
            stack.append((root,1))
        while stack:
            a,dep = stack.pop()
            #x.append((a,dep))
            graph[dep].append(a)
            if(a.left):
                stack.append((a.left,dep + 1))
            if(a.right):
                stack.append((a.right,dep + 1))
        for i in range(1,len(graph)+1):
            t = graph[i]
            t.reverse()
            for j in range(len(t)-1):
                t[j].next = t[j+1]
        
        #self.inorder(root)
        return root
