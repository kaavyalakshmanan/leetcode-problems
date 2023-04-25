class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # We want to return the max product of a contiguous subarray
        # Approach 1: Brute force - try every single possible subarray
            # this would cost us O(n^2)
        # Approach 2: Make use of patterns
            # if our subarray contained all positives, we can multiply everything and get the maxProduct
            # if our subarray contained all negatives, even number of -ves give us a positive, odd number of -ves give us a negative
            # we need to keep track of both maxProduct and minProduct
            # to get maxproduct of 3rd element, we have to get max product of the previous subproblem, which is first 2 elemenets
            # so for every num, we keep track of the max and min products at that num
            # if we get to a 0, we reset both max and min to 1

            # O(n) time O(1) space

        currMax, currMin = 1, 1
        res = max(nums)

        for num in nums:
            tmp = currMax
            # by making currMax and currMin also take max and min of num, we are autoamtically doing the resetting if we see a 0
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(tmp * num, currMin * num, num)
            res = max(res, currMax)

        return res
