class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        
        # O(m*n) time O(n) space
        
        def flip(arr):
            for i, num in enumerate(arr):
                if num == 0:
                    arr[i] = 1
                else:
                    arr[i] = 0
                    
            return arr
        
        for i, row in enumerate(grid):
            if row[0] == 1:
                grid[i] = flip(row)
        
        for row in range(len(grid)-1):
            if grid[row] != grid[row+1]:
                return False
            
        return True
