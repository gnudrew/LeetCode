class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # convert jewels to set (hashmap)
        jset = set(jewels)
        
        ans = 0
        for s in stones:
            if s in jset:
                ans += 1
        
        return ans