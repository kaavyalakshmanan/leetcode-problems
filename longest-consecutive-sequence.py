class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # O(n) time O(n) space

        # convert input array into set to make use of O(1) lookup time
        numsSet = set(nums)
        start = set()
        maxLen = 0

        for num in numsSet:
            # find all the starts for each sequence and add to another set
            if num-1 not in numsSet:
                start.add(num)

        for num in start:
            # find the length of the longest sequence starting at each start
            currLen = 0
            i = num
            while i in numsSet:
                currLen+=1
                i+=1

            maxLen = max(maxLen, currLen)

        return maxLen

        # another that doesnt invovle creating 2 separate sets

        numsSet = set(nums)
        maxLen = 0

        for num in numsSet:
            end, currLen = num, 1
            # if we have found a start
            if num-1 not in numsSet:
                while end+1 in numsSet:
                    end+=1
                    currLen+=1
            maxLen = max(currLen, maxLen)

        return maxLen

                




        

