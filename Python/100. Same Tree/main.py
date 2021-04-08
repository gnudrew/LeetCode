# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.ans = True
        def helper(p,q):
            if (not q) ^ (not p):
                self.ans = False
                return
            if p:
                if p.val != q.val:
                    self.ans = False
                    return
                helper(p.left, q.left)
                helper(p.right, q.right)
        helper(p,q)
        return self.ans