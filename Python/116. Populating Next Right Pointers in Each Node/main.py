"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # Create q, passing in root Node
        # Create time, noting that in a perfect binary tree, there are 2^n nodes in level n.
        if root is None:
            return root
        
        q = deque([root])
        time = 0 
        level = 0
        
        # Iterate:
        while q: 
            cur_node = q.popleft() # space: O(logN), time: #O(N)
            # Can we get space -> O(1)
            time += 1
            if time == 2**level:
                cur_node.next = None
                time = 0
                level += 1
            else:
                cur_node.next = q[0]
        ## add Node's children to the q
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            
        return root
            