class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    Inf = float('inf')
    def minDiffInBST(self, root): # -> int:
        self.best = Inf = self.Inf
        def dfs(n,a,b):
            if n:
                x = n.val
                self.best = min( self.best, x-a, b-x )
                dfs(n.left ,a,x)
                dfs(n.right,x,b)
        dfs(root,-Inf,Inf)
        return self.best

if __name__ == '__main__':
    root = TreeNode(val=4)
    root.left = TreeNode(val=2)
    root.left.left = TreeNode(val=1)
    root.left.right = TreeNode(val=3)
    root.right = TreeNode(val=6)

    s = Solution()
    print(s.minDiffInBST(root))        