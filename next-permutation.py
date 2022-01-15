class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # O(n) time O(1) space
        # Pointers
        
        # Step 1: Find strictly decreasing subsequence
        ptr1 = len(nums)-2
        while ptr1 >= 0 and nums[ptr1] >= nums[ptr1+1]:
            ptr1-=1
                
        # Step 2: Swap with next biggest
        ptr2 = len(nums)-1
        if ptr1 >= 0:
            while ptr2 > ptr1 and nums[ptr2] <= nums[ptr1]:
                ptr2-=1
                
            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            ptr2 = len(nums)-1
            
        # Step 3: Reverse strictly decreasing subsequence
        ptr1+=1
        while ptr1 < ptr2:
            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            ptr1+=1
            ptr2-=1
            
        return nums
            
                
        
