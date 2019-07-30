# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        stack = []
        s = []
        if root.val == x or root.val == y:
            s.append((root,1))
        if root:
            stack.append((root,1))
        while stack:
            new_root,dep = stack.pop()
            if(new_root.left):
                stack.append((new_root.left,dep+1))
                if(new_root.left.val == x or new_root.left.val == y):
                    s.append((new_root,dep+1))
            if(new_root.right):
                stack.append((new_root.right,dep+1))
                if(new_root.right.val == x or new_root.right.val == y):
                    s.append((new_root,dep+1))
        
        if(s[0][0].val != s[1][0].val and s[0][1] == s[1][1]):
            return True
        else:
            return False
