# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            root.left = None
            self.temp.right = root
            self.temp = root
            self.inorder(root.right)
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        new_root = self.temp = TreeNode(None)
        self.inorder(root)
        return new_root.right
