class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # O(logmn) time O(n) space
        # Binary Search
        
        def searchRow(row):
            start, end = 0, len(row)-1
            while start <= end:
                mid = (start+end)//2
                if row[mid] == target:
                    return True
                if row[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
            return False
        
        start, end = 0, len(matrix)
        while start <= end:
            mid = (start+end)//2
            if mid < 0 or mid >= len(matrix):
                return False
            currRow = matrix[mid]
            if target >= currRow[0] and target <= currRow[-1]:
                return searchRow(currRow)
            if target < currRow[0]:
                end = mid-1
            else:
                start = mid+1
            
        return False
                
