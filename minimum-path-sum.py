class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # O(m*n) time O(n) space
        # Bottom Up DP
        
        prevRow = [ i for i in grid[-1] ]
        for i in range(len(prevRow)-2, -1, -1):
            prevRow[i]+=prevRow[i+1]
        
        ROWS, COLS = len(grid), len(grid[0])
        
        for row in range(ROWS-2, -1, -1):
            currRow = [0] * len(grid[0])
            for col in range(COLS-1, -1, -1):
                if col == COLS-1:
                    currRow[col] = grid[row][col] + prevRow[col]
                else:
                    currRow[col] = min(currRow[col+1], prevRow[col]) + grid[row][col]
                    
            prevRow = currRow
            
        return prevRow[0]
