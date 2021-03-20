class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # slice array into slice1 and slice2
        slice1 = nums[:n]
        slice2 = nums[n:]
        # build new array alternating slice1 and slice2
        ans = []
        for i in range(n):
            ans.append(slice1[i])
            ans.append(slice2[i])
        # return
        return ans