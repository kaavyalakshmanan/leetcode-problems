class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # O(n) time O(n) space

        left = {}
        right = {}

        currSum = 0
        for i in range(len(nums)):
            left[i] = currSum
            currSum += nums[i]

        currSum = 0
        for i in range(len(nums)-1, -1, -1):
            right[i] = currSum
            currSum += nums[i]

        i = 0
        while i < len(nums):
            if left[i] == right[i]:
                return i
            i+=1

        return -1

        # more optimal solution: prefix sum
        # O(n) time O(1) space
        # instead of using 2 dictionaries and 3 loops, we can do this all in constant space and 1 loop
        # calculate the totalSum of nums
        # iterate forwards and keep track of leftSum so far
        # at each idx, what is the rightSum?
            # that would be totalSum - leftSum - nums[i] (since leftSum does not include nums[i])
            # if leftSum == rightSum, return i
        
        totalSum = sum(nums)
        leftSum = 0
        for i, n in enumerate(nums):
            rightSum = totalSum - leftSum - n
            if leftSum == rightSum:
                return i
            leftSum += n

        return -1
