class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # O(n) time O(1) space

        left, right = 0, 0
        count = 0
        prev = nums[0]
        
        while right < len(nums):
            while right < len(nums) and nums[right] == prev:
                count+=1
                right+=1
            if count >= 2:
                nums[left] = prev
                nums[left+1] = prev
                left+=2
            else:
                nums[left] = prev
                left+=1
            if right < len(nums):
                prev = nums[right] 
                count = 0

        return left


