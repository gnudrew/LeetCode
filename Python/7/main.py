class Solution(object):
    def reverse(self, x): # O(n)
        """
        :type x: int
        :rtype: int
        """
        # is x negative?
        isNegative = False
        if x < 0:
            isNegative = True
        
        # convert int to string, O(1)
        s = str(x)
        new_s = ""
        
        # iterate and append, O(n)
        if isNegative:
            r = range(len(s)-1)
        else:
            r = range(len(s))
        for i in r:
            new_s += s[len(s)-i-1]
        
        # convert str to int, O(1)
        new_x = int(new_s)
        if isNegative:
            new_x = -new_x
            
        # check in bounds and return
        if new_x >= -2**31  and new_x < 2**31:
            return new_x
        else:
            return 0