class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # O(n) time O(n) space
        
        modDict = { 0: -1 }
        cumSum = 0
        
        for i, num in enumerate(nums):
            cumSum += num
            rem = cumSum % k
            if rem in modDict:
                if i - modDict[rem] >= 2:
                    return True
            else:
                modDict[rem] = i
            
            
        return False
