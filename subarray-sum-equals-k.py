class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # O(n) time O(n) space
        # Prefix sum dict
        
        prefixSum = {}
        prefixSum[0] = 1
        output, res = 0, 0
        for num in nums:
            output+=num
            if output - k in prefixSum:
                res+= prefixSum[output - k]
            prefixSum[output] = 1 + prefixSum.get(output, 0)
                
        return res 
