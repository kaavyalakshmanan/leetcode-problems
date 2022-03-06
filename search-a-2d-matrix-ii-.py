class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # O(mlogn) time O(1) space
        
        # Step 2: Binary search
        def binarySearch(nums):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (right+left)//2
                if nums[mid] == target:
                    return True
                if nums[mid] < target: 
                    left = mid+1
                else:
                    right = mid-1
            return False
        
        # Step 1: Find row 
        row = len(matrix)-1
        while row >= 0:
            if matrix[row][0] <= target:
                break
            row-=1
        
        for i in range(row+1):
            currRow = matrix[i]
            if binarySearch(currRow):
                return True
            
        return False
