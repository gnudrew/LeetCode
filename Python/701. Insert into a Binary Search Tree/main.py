# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        #Empty tree case
        if root is None:
            return TreeNode(val=val)
        
        if val < root.val: 
            if root.left is None: #leaf
                root.left = TreeNode(val=val)
            else: #recursive step
                self.insertIntoBST(root.left,val)
        else:
            if root.right is None: #leaf
                root.right = TreeNode(val=val)
            else: #recursive step
                self.insertIntoBST(root.right,val)

        #return original root
        return root