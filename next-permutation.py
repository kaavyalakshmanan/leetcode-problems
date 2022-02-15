class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # O(n) time O(1) space
        
        # Find strictly decreasing subsequence
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
        
        # Swap with next biggest
        if i >= 0:
            j = len(nums)-1
            while j > i and nums[j] <= nums[i]:
                j-=1
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
        i+=1
        
        # Reverse strictly decreasing subsequence
        j = len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
            
        return nums
        
