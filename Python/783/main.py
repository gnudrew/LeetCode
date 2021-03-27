# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # get the closest value to the root in a given subtree
        def getClosestVal(n,branch=None):
            if branch == 'left':
            # max value is in right-most leaf
                # base case
                if n.left is None:
                    return None
                current = n.left
                while current.right:
                    current = current.right
                return current.val
            
            if branch == 'right':
            # min value is in left-most leaf
                # base case
                if n.right is None:
                    return None
                current = n.right
                while current.left:
                    current = current.left
                return current.val
        
        def preorder(n,curMinDiff):
            # base case
            if not n.left and not n.right:
                return
            # get left and right closest differences, if they exist
            if n.left:
                leftDiff = n.val - getClosestVal(n,branch='left')
            if n.right:
                rightDiff = getClosestVal(n,branch='right') - n.val
            # three cases for subtree existence
            if n.left and n.right:
                minDiff = min(leftDiff, rightDiff)
            elif n.left is None:
                minDiff = rightDiff
            else:
                minDiff = leftDiff
            curMinDiff[0] = min(minDiff, curMinDiff[0])
            
            preorder(n.left,curMinDiff)
            preorder(n.right,curMinDiff)
        
        curMinDiff=[10**5]
        preorder(root,curMinDiff)
        return curMinDiff[0]

if __name__ == '__main__':
    root = TreeNode(val=4)
    root.left = TreeNode(val=2)
    root.left.left = TreeNode(val=1)
    root.left.right = TreeNode(val=3)
    root.right = TreeNode(val=6)

    s = Solution()
    print(s.minDiffInBST(root))
