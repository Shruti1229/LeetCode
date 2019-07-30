# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leaves(root):
            if not root:
                return([])
            else:
                if root.left==None and root.right==None:
                    return([root.val])
                else:
                    return(leaves(root.left)+leaves(root.right))

        return(leaves(root1)==leaves(root2))

