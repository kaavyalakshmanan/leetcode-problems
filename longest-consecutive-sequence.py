class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # O(n) time O(n) space
        # Use set
        
        numSet = set(nums)
        output = 0
        
        for num in nums:
            curr = 0
            # Check whether num is the start of a sequence
            if num-1 not in numSet:
                while num in numSet:
                    curr+=1
                    num+=1
            output = max(output, curr)
            
        return output
                
