class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        # O(m*n) time O(n) space
        # DP
        
        ROWS, COLS = len(points), len(points[0])
        prevRow = [0] * COLS
        
        for row in range(ROWS):
            currRow = prevRow[:]
            for col in range(1, COLS):
                currRow[col] = max(currRow[col], currRow[col-1]-1)
            for col in range(COLS-2, -1, -1):
                currRow[col] = max(currRow[col], currRow[col+1]-1)
            for col in range(COLS):
                prevRow[col] = points[row][col] + currRow[col]
                
        return max(prevRow)
