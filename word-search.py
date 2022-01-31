class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # O(n*m*3^l) time O(l) space
        
        def dfs(row, col, idx):
            if idx == len(word):
                return True
            if row < 0 or row == ROWS or col < 0 or col == COLS:
                return False
            if board[row][col] != word[idx]:
                return False
            if (row, col) in visited:
                return False
            
            visited.add((row, col))
            match = (
                dfs(row+1, col, idx+1) or 
                dfs(row-1, col, idx+1) or
                dfs(row, col+1, idx+1) or
                dfs(row, col-1, idx+1)
            )
            
            visited.remove((row, col))
            return match
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False
