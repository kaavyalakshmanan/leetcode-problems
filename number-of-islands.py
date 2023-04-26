class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # O(n*m) time O(n*m) space
        # DFS

        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(row, col):
            if row < 0 or row == rows or col < 0 or col == cols:
                return 
            if grid[row][col] == "0":
                return
            if (row, col) in visited:
                return

            visited.add((row, col))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    res +=1

        return res
