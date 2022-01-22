class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # O(n) time O(n) space
        # One pass hash
        
        compDict = {}
        for i, num in enumerate(nums):
            if num in compDict:
                return [i, compDict.get(num)]
            compDict[target-num] = i
