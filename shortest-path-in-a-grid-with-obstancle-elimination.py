class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        # O(m*n) time O(m*n) space
        # BFS
        
        q = collections.deque([(0, 0, 0)])
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        pathLen = 0
        
        while q:
            qLen = len(q)
            for i in range(qLen):
                row, col, numObst = q.popleft()
                if row == ROWS-1 and col == COLS-1 and numObst <= 1:
                    return pathLen

                directions = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
                visit.add((row, col))
                for dr, dc in directions:
                    if dr < 0 or dr == ROWS or dc < 0 or dc == COLS or (dr, dc) in visit:
                        continue
                    if grid[dr][dc] == 1:
                        q.append((dr, dc, numObst+1))
                    else:
                        q.append((dr, dc, numObst))
                        
            pathLen+=1
            
        return -1
                    
            
