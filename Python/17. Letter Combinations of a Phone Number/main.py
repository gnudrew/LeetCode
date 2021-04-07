class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        """
        Example 1:
        Input: digits = "23"
        Output: ["a","b","c"]
        
        Example 2:
        Input: digits = "925"
        Output: ["waj","xaj","yaj","zaj",...]
        """
        if not digits:
            return []
        
        # Hash Map approach
        m2 = "abc"
        m3 = "def"
        m4 = "ghi"
        m5 = "jkl"
        m6 = "mno"
        m7 = "pqrs"
        m8 = "tuv"
        m9 = "wxyz"
        
        h = {
            '2':m2,
            '3':m3,
            '4':m4,
            '5':m5,
            '6':m6,
            '7':m7,
            '8':m8,
            '9':m9
        }
        
        # first digit
        ans = [i for i in h[digits[0]]]
        if len(digits) == 1:
            return ans
        
        # subsequent digits
        for dig in digits[1:]: #iterate thru each digit from input list
            tmp = [part + h[dig][0] for part in ans] +\
            [part + h[dig][1] for part in ans] +\
            [part + h[dig][2] for part in ans]
            
            if len(h[dig]) == 4:
                tmp += [part + h[dig][3] for part in ans]
            ans = tmp # reassign ans pointer
        return ans
