class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        def bfs(row, col, numHouses):
            
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            ROWS, COLS = len(grid), len(grid[0])
            minDist = 0
            housesReached = 0
            
            q = collections.deque([(row, col)])
            visit = set()
            visit.add((row, col))
            
            pathLen = 0
            while q and housesReached < numHouses:
                qLen = len(q)
                for i in range(qLen):
                    x, y = q.popleft()
                    
                    # We reached a house
                    if grid[x][y] == 1:
                        minDist += pathLen
                        housesReached+=1
                        continue
                        
                    # We reached an empty
                    for dr, dc in directions:
                        newRow, newCol = x + dr, y + dc
                        if newRow >= 0 and newRow < ROWS and newCol >= 0 and newCol < COLS:
                            if (newRow, newCol) not in visit and grid[newRow][newCol] != 2:
                                visit.add((newRow, newCol))
                                q.append((newRow, newCol))
                                
                pathLen +=1
                
            # If we did not reach all houses
            if housesReached < numHouses:
                for row in range(ROWS):
                    for col in range(COLS):
                        if grid[row][col] == 0 and (row, col) in visit:
                            grid[row][col] = 2
                            
                return inf
            
            # Return minDist if we reached all houses
            return minDist
        
        minDist = inf
        ROWS, COLS = len(grid), len(grid[0])
        numHouses = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    numHouses+=1
                    
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    minDist = min(minDist, bfs(row, col, numHouses))
        
        if minDist == inf:
            return -1
        
        return minDist

        
#         directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#         ROWS, COLS = len(grid), len(grid[0])
#         total = [[0] * COLS] * ROWS
        
#         emptyLandValue = 0
#         minDist = inf
        
#         for row in range(ROWS):
#             for col in range(COLS):
                
#                 # Start a new BFS from each house
#                 if grid[row][col] == 1:
#                     # minDist = inf
                    
#                     q = collections.deque([(row, col)])
#                     steps = 0
                    
#                     while q:
#                         steps+=1
#                         qLen = len(q)
#                         for level in range(qLen):
#                             x, y = q.popleft()
                            
#                             for dr, dc in directions:
#                                 nextRow, nextCol = x + dr, y + dc
                                
#                                 # For each cell with value of emptyLandValue, add dist and decrement cell by 1
#                                 if nextRow >= 0 and nextRow < ROWS and nextCol >= 0 and nextCol < COLS and grid[nextRow][nextCol] == emptyLandValue:
#                                     grid[nextRow][nextCol]-=1
#                                     total[nextRow][nextCol] += steps
#                                     q.append((nextRow, nextCol))
#                                     minDist = min(minDist, total[nextRow][nextCol])
                                    
#                         emptyLandValue -=1
#                 print(minDist)
                        
#             return minDist if minDist != inf else -1
                                
        
        
                    
            
        
        
