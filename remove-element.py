class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # O(n) time O(1) space
        # 2 pointer

        start, end = 0, len(nums)-1

        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end-=1
            else:
                start+=1

        return start
        
