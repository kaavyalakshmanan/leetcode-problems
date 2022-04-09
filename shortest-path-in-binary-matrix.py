class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # O(n^2) time O(n^2) space
        # BFS
        
        ROWS, COLS = len(grid), len(grid)
        
        # Base cases
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        
        q = collections.deque([(0, 0)])
        pathSize = 1
        
        # up, down, left, right, diag up left, diag up right, diag down left, diag down right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        visit = set()
        
        while q:
            qLen = len(q)
            for i in range(qLen):
                x, y = q.popleft()
                if x == ROWS-1 and y == COLS-1:
                    return pathSize
                for dr, dc in directions:
                    row, col = x + dr, y + dc
                    if row < 0 or col < 0 or row == ROWS or col == COLS:
                        continue
                    if grid[x+dr][y+dc] == 1:
                        continue
                    if (row, col) in visit:
                        continue
                    visit.add((row, col))
                    q.append((row, col))
            pathSize+=1
            
        return -1
                        
                
