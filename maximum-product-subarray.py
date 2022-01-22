class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # O(n) time O(1) space
        # DP
        
        minVal, maxVal = 1, 1
        output = max(nums)
        for num in nums:
            temp = minVal * num
            minVal = min(minVal * num, maxVal * num, num)
            maxVal = max(temp, maxVal * num, num)
            output = max(minVal, maxVal, output)
            
        return output 
