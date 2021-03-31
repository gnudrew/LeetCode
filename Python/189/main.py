class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size == 1:
            return nums
        
        # Method 1: Item assignment
        ans = [0]*size
        for i in range(size):
            print("nums is:",nums)
            print("i is:",i)
            print("nums[i-k] is:",nums[i-k])
            ans[i] = nums[i-k]
            print("ans is:",ans)
        print("FINAL ANS:",ans)
        
        return ans

s = Solution()
print(s.rotate([1,2,3],1))