class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # O(n) time O(1) space
        # Bottom Up DP
        
        jumpIdx = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= jumpIdx:
                jumpIdx = i
        
        return jumpIdx == 0
