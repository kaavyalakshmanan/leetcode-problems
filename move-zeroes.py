class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # O(n) time O(1) space
        # 2 pointers
        
        zero, nonZero = 0, 0
        
        while nonZero < len(nums):
            while zero < len(nums) and nums[zero] != 0:
                zero+=1
            while nonZero < len(nums) and nums[nonZero] == 0:
                nonZero+=1
            if zero < len(nums) and nonZero < len(nums):
                if zero < nonZero:
                    nums[zero], nums[nonZero] = nums[nonZero], nums[zero]
                else:
                    zero, nonZero = nonZero, zero
            zero+=1
            nonZero+=1
            
        
                
                
