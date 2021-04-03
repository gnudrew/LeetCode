# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global D #diameter
        D = 0
        self.longest(root)
        
        return D
        
    def longest(self,node):
        #terminating condition
        if node is None:
            return 0
        
        #DFS steps
        depth_left = self.longest(node.left)
        depth_right = self.longest(node.right)
        
        # process current node
        global D
        D = max(D,depth_left+depth_right)
        
        # output to parent node
        return max(depth_left,depth_right)+1
        