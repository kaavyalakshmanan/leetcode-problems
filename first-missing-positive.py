class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # O(n) time O(1) space

        # Step 1: Replace anything <= 0 with len(nums)+1

        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = len(nums)+1

        # Step 2: Mark array in place
        for i, num in enumerate(nums):
            currIdx = abs(num)-1
            if currIdx < len(nums) and nums[currIdx] > 0:
                nums[currIdx] *= (-1)

        # Step 3: Find first missing positive 
        for i, num in enumerate(nums):
            if num > 0:
                return i+1

        return len(nums)+1

        
