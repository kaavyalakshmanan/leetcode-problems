class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        # O(n) time O(1) space

        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                k-=1
            if k < 0:
                if nums[left] == 0:
                    k+=1
                left+=1
            right+=1

        return right-left

