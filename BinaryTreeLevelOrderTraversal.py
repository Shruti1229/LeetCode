# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        stack = []
        s = []
        if root:
            stack.append((root,1))
        while stack:
            new_root , dep = stack.pop()
            graph[dep].append(new_root.val)
            if(new_root.left):
                stack.append((new_root.left,dep+1))
            if(new_root.right):
                stack.append((new_root.right,dep + 1))
        #print(graph)
        k = []
        for i in range(1,len(graph)+1):
            t = graph[i]
            t.reverse()
            k.append(t)
        return k
