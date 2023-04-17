class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # DFS Backtracking
        # O(n*m*4^l) where n = rows m = cols and l = len(word) time
        # O(l) space because recurses to length of word

        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(row, col, idx):

            if idx == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[idx] or (row, col) in visited:
                return False

            visited.add((row, col))

            res = dfs(row, col-1, idx+1) or dfs(row, col+1, idx+1) or dfs(row-1, col, idx+1) or dfs(row+1, col, idx+1)

            visited.remove((row, col))

            return res


        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False



            



            



