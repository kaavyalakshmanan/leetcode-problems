class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # O(n) time O(1) space
        # Sliding window
        
        left, right = 0, 0
        res = 0
        maxRes = -inf
        

        while right < len(nums):
            currSum = res + nums[right]
            if nums[right] > currSum:
                res = nums[right]
                left = right
            else:
                res = currSum
            maxRes = max(maxRes, res)
            right+=1

        return maxRes
