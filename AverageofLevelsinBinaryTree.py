# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict 
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = 0
        stack = []
        graph = defaultdict(list)
        if not root:
            return 0
        if root:
            stack.append((root,1))
        while stack:
            new_root,dep = stack.pop()
            ans=dep
            graph[ans].append(new_root.val)
            if new_root.left:
                stack.append((new_root.left,dep+1))
            if new_root.right:
                stack.append((new_root.right,dep+1))
        a = []
        for i in range(1,len(graph)+1):
            t = graph[i]
            sum = 0.0
            for j in t:
                sum = sum + j
            a.append(sum/len(t))
        return a
