# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        self.prev = None
        self.next_left = None
        
        def preorder(root): # assigning all left pointers
            if root is not None:
                self.next_left = root.left
                root.left = self.prev
                self.prev = root
                preorder(self.next_left)
                preorder(root.right)
        
        def cycleBack(pointer):
            """
            :type pointer: TreeNode
            :rtype head: TreeNode
            """
            while pointer.left:
                pointer.left.right = pointer
                pointer = pointer.left
                pointer.right.left = None
                
            return pointer
        
        preorder(root)
        return cycleBack(self.prev)