class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(n) time O(n) space
        # Forwards & backwards

        answer = [1] * len(nums)
        prefix, postfix = nums[0], 1

        for i in range(1, len(nums)):
            answer[i] = prefix
            prefix*= nums[i]

        for i in range(len(nums)-2, -1, -1):
            postfix*= nums[i+1]
            answer[i] *= postfix

        return answer
        
