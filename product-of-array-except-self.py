class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # O(n) time O(1) space
        # Product arrays
        
        prefix = nums[0]
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = prefix
            prefix *= nums[i]
            
        postfix = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
            
        return output
