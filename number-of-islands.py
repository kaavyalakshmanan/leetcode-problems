class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # O(m*n) time O(m*n) space
        # BFS
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        numIslands = 0
        
        def bfs(row, col):
            q = collections.deque()
            visited.add((row, col))
            q.append((row, col))
            
            while q:
                r, c = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for dr, dc in directions:
                    newRow, newCol = r+ dr, c + dc
                    
                    if newRow in range(ROWS) and newCol in range(COLS) and grid[newRow][newCol] == "1" and (newRow, newCol) not in visited:
                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))
                        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    numIslands+=1
                    
        return numIslands
                
