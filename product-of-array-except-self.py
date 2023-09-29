class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(n) time O(n) space
        # Prefix and postfix

        prefix, postfix = nums[0], 1
        res = [1] * len(nums)

        for i in range(1, len(res)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(res)-2, -1, -1):
            postfix *= nums[i+1]
            res[i] *= postfix

        return res


        
        
