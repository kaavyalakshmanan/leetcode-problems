class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # O(n) time O(n) space
        # Bottom Up DP
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]
        
        maxAmt = max(dp[-1], dp[-2])
        
        for i in range(len(nums)-3, -1, -1):
            second = nums[i] + dp[i+2] 
            third = nums[i] + dp[i+3] if i+3 < len(nums) else 0
            dp[i] = max(second, third)
            maxAmt = max(maxAmt, dp[i])
        
        return maxAmt

        # O(n) time O(1) space
        # Bottom Up DP w/ Space Optimization
        
        if len(nums) == 1:
            return nums[0]
        
        maxAmount = max(nums[-1], nums[-2])
        for i in range(len(nums)-3, -1, -1):
            second = nums[i] + nums[i+2] 
            third = nums[i] + nums[i+3] if i+3 < len(nums) else 0
            nums[i] = max(second, third)
            maxAmount = max(maxAmount, nums[i])
        
        return maxAmount
            
            
    
    
    
