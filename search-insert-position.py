class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # O(logn) time O(1) space
        # Binary Search
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
                
        return left+1 if target > nums[left] else left
