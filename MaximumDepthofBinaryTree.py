# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if not root:
            return 0
        DFS = [] 
        DFS.append((root,1))
        while DFS:
            root, depth = DFS.pop()
            if depth > ans:
                ans = depth
            if root.left:
                DFS.append((root.left, depth + 1))
            if root.right:
                DFS.append((root.right, depth + 1))
        return ans
