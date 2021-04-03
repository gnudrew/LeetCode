# from collections import Count as c

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # # Brute Force approach
        # if not A or not B or not C or not D:
        #     return 0
        # counter = 0
        # for a in A: # Time ~ O(N^4)
        #     for c in C:
        #         for b in B:
        #             for d in D:
        #                 if a+c+b+d == 0:
        #                     counter += 1
        # return counter
    
        # The idea is: count how many times a+b == -c-d
    
        # # Counter object approach
        # counter = collections.Counter()
        # for a in A: #T~ O(N^2)
        #     for b in B:
        #         counter.update([a+b])
        # ans = 0
        # for c in C: #T ~ O(N^2)
        #     for d in D:
        #         if -(c+d) in counter:
        #             ans += counter[-c-d]
        # return ans
    
        # # Incredible 2-line approach
        # AB = collections.Counter(a+b for a in A for b in B)
        # return sum(AB[-c-d] for c in C for d in D)
    
        # Normal hashmap approach
        h = {}
        for a in A:
            for b in B:
                ab = a + b
                if ab in h:
                    h[ab] += 1
                else:
                    h[ab] = 1
        ans = 0
        for c in C:
            for d in D:
                cd = -c-d
                if cd in h:
                    ans += h[cd]
        return ans
        