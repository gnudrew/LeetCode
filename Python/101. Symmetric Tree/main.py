# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Do iterative inorder traversal of Left subtree.
        # Simulatenously traverse Right subtree in mirror fashion.
        
        # I first setup an inorder iterative traversal, then added the other side.
        # Start parallel traversals from the children of root.
            
        # Null edge case
        if root is None:
            return True

        # Initialize variables
        stackL, stackR = [], []
        curNodeL = root.left; curNodeR = root.right

        # Opening edge case
        if bool(curNodeL) ^ bool(curNodeR):
            return False

        while (stackL or stackR or curNodeL or curNodeR):
            # go as far as possible in one direction
            while curNodeL or curNodeR:
                # if one node exists and the other doesn't, tree is not a mirror
                if not curNodeL or not curNodeR:
                    return False
                stackL.append(curNodeL); stackR.append(curNodeR)
                curNodeL, curNodeR = curNodeL.left, curNodeR.right

            # pop, read, point opposite
            curNodeL, curNodeR = stackL.pop(), stackR.pop()
            if curNodeL.val != curNodeR.val:
                return False
            curNodeL, curNodeR = curNodeL.right, curNodeR.left

        # If we finish, tree is a mirror
        return True