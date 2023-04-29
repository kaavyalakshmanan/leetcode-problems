class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # in order to get the product of everything ezxcept self in O(n) time and O(1) space, we need to compute the left product and the right product
            # aka, the product of everything except self when we iterate from the left
            # and then the product of everything except self when we interate from the right
            # then at an arbitrary index, we would multiply the left and right
            # which would give us total product of everything except self

            # O(n) time O(1) space

        prefix, postfix = 1, 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
