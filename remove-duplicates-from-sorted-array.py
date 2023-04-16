class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # O(n) time O(1) space
        
        left, right = 0, 0

        while right < len(nums):
            if nums[left] != nums[right]:
                left, right = left+1, right+1
            else:
                while right < len(nums) and nums[left] == nums[right]:
                    right+=1
                if right < len(nums):
                    nums[left+1] = nums[right] 
                    left+=1

        return left+1
