class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # in this problem we are given an n x m board with "X"s and "O"s, and we want to flip the Os to Xs if they are 4-directionally surrounded by Xs
        # aka up down left right
        # NOT diagonal
        # so if there is O in the border that cant be flipped to an X
        # alternatively if there is an O in a nonborder that is NOT 4 directionally surrounded by Xs that cant be flipped either

        # one approach is to run BFS on every O and check if it is 4 directionally surrounded by X
        # with this apporach if we find a cluster of Os and we would keep going until we find the Xs on all 4 sides (flip them all to X) or we dont because we either hit the border or there are Xs on all 4 sides (dont flip them)
        # but this approach can get complicated

        # second approach: urtilize REVERSE THINKING
        # the problem asks us to find surrouned regions and flip them
        # aka we want to capture surrounded regions
        # another way to state this is to say "caputure everything except unsurrounded regions"
            # where an unsurrounded region is a region that is either in the border or is not 4-directionally surrounded by Xs
        # so step 1: iterate over the borders and change all Os to Ts, and run DFS on each border O and change neighbors to Ts
        # step 2: second iteration over board, change all remaining Os to Xs
        # step 3: third iteration over board, change all Ts back to Os
        # boom, done

        rows, cols = len(board), len(board[0])
        visited = set()

        # helper thats used by step 1
        # turn all Os to Ts
        def dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0:
                return

            if (row, col) in visited:
                return

            if board[row][col] == "X":
                return
            
            board[row][col] = "T"
            visited.add((row, col))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        
        # step 1: change border Os to Ts and run dfs on each border O
        # top row, bottom row
        for c in range(cols):
            if board[0][c] == "O":
                # change this guy and all his neighbors to X
                dfs(0, c)
            k = (rows-1, c)
            l = board[rows-1][c]
            if board[rows-1][c] == "O":
                dfs(rows-1, c)

        # left column, right column
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols-1] == "O":
                dfs(r, cols-1)

        # step 2: iterate over board, change remaining Os to Xs
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                if board[row][col] == "O":
                    board[row][col] = "X"

        # step 3: final iteration over board, change Ts back to Os
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"




