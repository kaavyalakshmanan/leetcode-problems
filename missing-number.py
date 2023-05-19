class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # O(n) time O(1) space

        for i, n in enumerate(nums):
            idx = abs(n)
            if idx == len(nums):
                continue
            if idx == len(nums)+1:
                idx = 0
            if nums[idx] == 0:
                nums[idx] = (len(nums)+1) * (-1)
            else:
                nums[idx] *= (-1)
            
        for i, n in enumerate(nums):
            if n >= 0:
                return i

        return len(nums)
