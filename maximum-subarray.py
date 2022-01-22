class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # O(n) time O(1) space
        # Sliding window
        
        left, right = 0, 0
        currSum, maxSum = 0, max(nums)
        while right < len(nums):
            currSum += nums[right]
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
                left = right+1
            right+=1
            
        return maxSum
