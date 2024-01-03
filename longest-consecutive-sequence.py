class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # O(n) time O(n) space
        # Use hashset
        
        numsSet = set(nums)
        longestStreak = 0

        for num in nums:
            if num-1 not in numsSet:
                currNum, currLongest = num, 0
                while currNum in numsSet:
                    currNum+=1
                    currLongest+=1

                longestStreak = max(longestStreak, currLongest)

        return longestStreak
