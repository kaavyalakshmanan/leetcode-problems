class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # O(logn) time O(1) space
        # Binary Search
        
        def findTarget(left, right, first):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    if first:
                        if mid == left or nums[mid-1] != target:
                            return mid
                        right = mid
                    else:
                        if mid == right or nums[mid+1] != target:
                            return mid
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
                    
            return -1
        
        
        firstPos = findTarget(0, len(nums)-1, True)
        if firstPos == -1:
            return [-1, -1]
        lastPos = findTarget(firstPos, len(nums)-1, False)
        return [firstPos, lastPos]
