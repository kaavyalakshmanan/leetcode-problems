class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # O(n) time O(1) space

        for i, num in enumerate(nums):
            idx = abs(num)-1
            if nums[idx] > 0:
                nums[idx] *= (-1)
        
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)

        return res
