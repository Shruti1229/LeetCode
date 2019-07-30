# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.s = []
    def inorder(self,root,L,R):
        if(root):
            self.inorder(root.left,L,R)
            if(root.val >= L and root.val <= R):
                self.s.append(root.val)
            self.inorder(root.right,L,R)
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.inorder(root,L,R)
        x = sum(self.s)
        return (x)
