class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # O(n) time O(1) space

        lessThan = True
        for i in range(len(nums)):
            if i == len(nums)-1:
                break
            if (lessThan and nums[i] > nums[i+1]) or (not lessThan and nums[i] < nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            lessThan = not lessThan

