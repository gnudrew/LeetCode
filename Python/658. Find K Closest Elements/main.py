class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        size = len(arr)
        # Simple Case:
        if size == 1:
            return arr
        
        i = self.binarySearch(arr,x)
        # More Simple Cases
        if i == 0:
            return arr[:k]
        if i == size - 1:
            return arr[-k:]
        if size == 1:
            return arr
        
        # Main part
        a, b = i-1, i+1
        ans = [arr[i]]
        for _ in range(k-1):
            if abs(arr[a]-x) < abs(arr[b]-x) or abs(arr[a]-x) == abs(arr[b]-x):
                # value at a is closer
                ans.append(arr[a])
                a -= 1
            else:
                # value at b is closer
                ans.append(arr[b])
                b += 1
                b %= size
        
        return sorted(ans)            
    
    def binarySearch(self, arr, x):
        # return the index of x in the list.
        # If x is not in the list, return the index of the closest value to x in the list.
        # If x is equally close to two values, choose the lower one.
        a, b = 0, len(arr)-1
        while True:
            i = (a+b)//2
            if arr[b] == x:
                return b
            if arr[i] == x:
                return i
            if b - a <= 1:
                # return index of closer value to x
                if abs(arr[a]-x) <= abs(arr[b]-x):
                    return a
                else:
                    return b
            if x < arr[i]:
                b = i
            else:
                a = i