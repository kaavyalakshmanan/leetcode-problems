class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # O(n) time O(n) space

        res = [0] * (len(nums) * 2)
        n = len(nums)

        for i in range(n):
            res[i] = nums[i]
            res[i+n] = nums[i]

        return res
