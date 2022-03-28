class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # O(n) time O(n) space
        # Prefix sum
        
        prefixSum = { 0: 1 }
        res, count = 0, 0
        
        for num in nums:
            res += num
            if res - k in prefixSum:
                count += prefixSum[res - k]
            prefixSum[res] = 1 + prefixSum.get(res, 0)
            
        return count 
