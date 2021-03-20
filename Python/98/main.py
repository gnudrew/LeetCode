# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# import numpy as np

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_subtree(root)
    
    def check_subtree(self,node,upper=2**31,lower=-2**31-1):
        
        if node is None:
            return True
        
        if node.val <= lower or node.val >= upper:
            return False
        
        return ((self.check_subtree(node.left,lower=lower,upper=node.val)) 
                and (self.check_subtree(node.right,lower=node.val,upper=upper)))
        
