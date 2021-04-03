class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        center = edges[0][0]
        next_nodes = set(edges[1])
        if center in next_nodes:
            return center
        else:
            return edges[0][1]
        
            