class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        # O(n*k) time O(n*k) space
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = collections.deque([(0, 0, 0)])
        pathLen = 0
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        while q:
            qLen = len(q)
            
            for i in range(qLen):
                x, y, numK = q.popleft()
                visit.add((x, y))
                
                if x == ROWS-1 and y == COLS-1 and numK <= k:
                    return pathLen
                for dr, dc in directions:
                    r, c = x + dr, y + dc
                    if r < 0 or r == ROWS or c < 0 or c == COLS:
                        continue
                    if (r,c) in visit:
                        continue
                    if grid[r][c] == 1:
                        q.append((r, c, numK+1))
                    else:
                        q.append((r, c, numK))
            pathLen+=1
            
        
      
        return -1
