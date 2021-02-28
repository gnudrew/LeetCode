class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {} # keys are numbers, values are indices
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in hashmap:
                return [i, hashmap[num2]]
            else:
                hashmap[num1] = i
                    

            