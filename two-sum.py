class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # O(n) time O(n) space
        # Hash map
        # Note: "You may assume that each input would have exactly one solution" implies there are no duplicates

        compDict = {}
        for i, num in enumerate(nums):
            comp = target-num
            # case 1: We found match
            if (comp) in compDict:
                return [compDict[comp], i]
            # case 2: no match
            compDict[num] = i
