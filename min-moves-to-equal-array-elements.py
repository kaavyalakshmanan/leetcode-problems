class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        # Approach 1: Sorting
        # O(nlogn) time O(n) space
        
        nums.sort()
        count = 0
        
        for i in range(len(nums)-1, -1, -1):
            count+= (nums[i] - nums[0])
            
        return count 
    
        # Approach 2: Without sorting
        # O(n) time O(1) space
        
        minVal = min(nums)
        count = 0
        
        for i in range(len(nums)):
            count+= (nums[i] - minVal)
            
        return count
