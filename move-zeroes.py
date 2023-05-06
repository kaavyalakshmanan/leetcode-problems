class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # O(n) time O(1) space
        # Partitioning 

        left, right = 0, 0

        while left < len(nums) and nums[left] != 0:
            left+=1

        right = left+1

        while right < len(nums):
            while left < right and nums[left] != 0:
                left+=1
            while right < len(nums) and nums[right] == 0:
                right+=1
            if right == len(nums):
                break
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right+=1
