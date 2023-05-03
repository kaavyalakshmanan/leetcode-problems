class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        # we are given an array and a k, and we want to return true if there exists a contiguous subarray of at least length 2 whose sum is a multiple of k, false otherwise
        # heres some math properties that will help:
            # look at eg: nums = [23,2,4,6,7], k = 6
            # initially we have 23
            # 23 % 6 = 5
            # lets say we have a hashmap where key = %, value is idx
            # so now our hashmap contains (5, 0)
            # then we go to idx 1
            # 23 + 2 = 25
            # 25 % 6 = 1 --> add (1, 1) to hashmap
            # 25 + 4 = 29
            # 29 % 6 = 5 --> we try to add (5, 2) to hashmap, but key 5 already exists
            # this means that are exists a subarray that sums up to a multiple of k
            # so if we take difference between curr idx and that key's value --> 2 - 0 = 2, which means the length of that subarray is 2 which means we can return true

            # O(n) time O(n) space

        numsDict = { 0: -1 }
        currSum = 0

        for i, num in enumerate(nums):
            currSum += num
            if currSum % k not in numsDict:
                numsDict[currSum % k] = i
            else:
                if i - numsDict[currSum % k] >= 2:
                    return True

        return False
