class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            s = str(x)
            for i in range(len(s)//2): # omit center index if odd length
                if s[i] != s[-1-i]:
                    return False
            return True