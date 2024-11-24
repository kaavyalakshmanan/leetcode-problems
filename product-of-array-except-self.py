class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(n) time O(n) space if we count res arr
        # Iterate forwards & backwards
        
        res = [1] * len(nums)
        productSoFar = 1

        # Step 1: iterate backwards
        for i in range(len(nums)-1, -1, -1):
            res[i] = productSoFar
            productSoFar *= nums[i]

        # Step 2: Iterate forwards
        productSoFar = 1
        for i in range(len(nums)):
            res[i] *= productSoFar
            productSoFar *= nums[i]

        return res
