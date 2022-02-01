class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # O(n^2) time O(n) space
        # DP
        
        dp = [1] * (len(nums))
        output = 1
        
        for i in range(len(nums)-2, -1, -1):
            j = i+1
            curr = 1
            while j < len(nums): 
                if nums[j] > nums[i]:
                    curr = max(curr, dp[j] + 1)  
                j+=1
            dp[i] = curr
            output = max(output, dp[i])
                
        return output 
