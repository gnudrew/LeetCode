# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        s = []
        n = root
        
        while s or n:
            go_right = not n
            if go_right:
                n = s.pop()
                ans.append(n.val) #data
                n = n.right
            else:
                s.append(n)
                n = n.left
        
        return ans