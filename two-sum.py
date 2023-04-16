class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # O(n) time O(n) space
        # Hashmap
        
        compDict = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in compDict:
                compDict[nums[i]] = i
            else:
                return [compDict[comp], i]
