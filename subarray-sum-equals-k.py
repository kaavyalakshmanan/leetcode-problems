class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # O(n) time O(n) space
        # Prefix Sum
        
        prefixSum = { 0: 1 }
        totalSum, count = 0, 0
        
        for num in nums:
            totalSum += num
            target = totalSum - k
            if target in prefixSum:
                count += prefixSum[target]
            
            prefixSum[totalSum] = 1 + prefixSum.get(totalSum, 0)
            
        return count 
