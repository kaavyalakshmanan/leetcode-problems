class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # O(n) time O(1) space
        # 2 pointer

        left, right = 0, 1

        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left]:
                right+=1
            if right < len(nums):
                left+=1
                if left < right:
                    nums[left] = nums[right]
                right+=1



        return left+1
