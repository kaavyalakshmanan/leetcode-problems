class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # O(n) time O(1) space
        
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] == 0:
                nums[i] = len(nums)+1
        
        for i in range(len(nums)):
            currIdx = abs(nums[i])
            if currIdx > 0 and currIdx <= len(nums) and nums[currIdx-1] > 0:
                nums[currIdx-1] = nums[currIdx-1] * (-1) 
            elif currIdx == 0 and currIdx-1 >= 0:
                nums[currIdx-1] = len(nums)+1
                
        for i in range(len(nums)):
            currNum = nums[i]
            if currNum > 0:
                return i+1
            
        return len(nums)+1
            
