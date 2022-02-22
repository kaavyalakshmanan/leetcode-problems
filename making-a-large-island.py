class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        # O(n^4) time O(n^2) space
        
        ROWS, COLS = len(grid), len(grid)
        islandNum = 2
        maxIslandSize = 0
        islandMap = {}
        
        def floodFill(row, col, islandNum):
            islandSize = 1
            if row < 0 or col < 0 or row == ROWS or col == COLS:
                return 0
            if grid[row][col] == 0 or grid[row][col] == islandNum:
                return 0
            
            grid[row][col] = islandNum
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for dr, dc in directions:
                islandSize+=floodFill(row+dr, col+dc, islandNum)
                
            return islandSize
                
        def mergeIslandSize(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS:
                return 0
            islandSize = 1
            visit = set()
            
            directions = [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]
            
            for dr, dc in directions:
                if dr < 0 or dr == ROWS or dc < 0 or dc == COLS:
                    continue
                if grid[dr][dc] == 0:
                    continue
                if grid[dr][dc] in visit:
                    continue
                visit.add(grid[dr][dc])
                islandSize += islandMap[grid[dr][dc]]
                
            return islandSize
            

        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    islandSize = floodFill(row, col, islandNum)
                    islandMap[islandNum] = islandSize
                    maxIslandSize = max(maxIslandSize, islandSize)
                    islandNum+=1
                    
                    
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    islandSize = mergeIslandSize(row, col)
                    maxIslandSize = max(maxIslandSize, islandSize)
                    
        return maxIslandSize
                
        
