class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # O(n) time O(n) space
        # One pass hash
        
        compDict = {}
        for i in range(len(nums)):
            if nums[i] not in compDict:
                compDict[target-nums[i]] = i
            else:
                return [compDict[nums[i]], i]
