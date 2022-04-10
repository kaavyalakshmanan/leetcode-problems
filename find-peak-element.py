class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # O(logn) time O(1) space
        # Binary Search
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l+r)//2
            left = nums[m-1] if m-1 >= 0 else -inf
            right = nums[m+1] if m+1 < len(nums) else -inf
            if nums[m] > left and nums[m] > right:
                return m
            if right > left:
                l = m + 1
            else:
                r = m-1
