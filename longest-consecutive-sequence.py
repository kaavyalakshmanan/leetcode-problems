class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # O(n) time O(n) space
        # HashSet
        
        numsSet = set(nums)
        count = 0

        for num in nums:
            if num-1 in numsSet:
                continue
            j = num+1
            currCount = 1
            while j in numsSet:
                j+=1
                currCount+=1
            count = max(count, currCount)

        return count
