class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # O(n) time O(n) space
        # hash set and intelligent sequence building
        
        numsSet = set(nums)
        count = 0
        for n in nums:
            if n-1 in numsSet:
                continue
            j = n+1
            currCount = 1
            while j in numsSet:
                currCount+=1
                j+=1
            count = max(count, currCount)

        return count
