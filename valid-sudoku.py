class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # # in order to solve this problem, its important to undertand the rules of sudoku
        # # sudoku is a 9x9 grid
        # # every row must contain digits from 1-9 and no digit can repeat
        # # every column must contain digits from 1-9 and no digit can repeat
        # # sudoku is further divided into 9 3x3 grids and every 3x3 grid must contain digits from 1-9 and no digit can repeat
        # # the catch here is, not every cell will have a value
        # # so if a cell is empty, we can ignore it and it doesnt do anything to determine validity of the sudoku board
        # # return true if board is valid, else false

        # # lets break this problem up into 3 parts

        # rows, cols = len(board), len(board[0])

        # # part 1: determine validity of each row based on above condition
        # # lets create a hashset for every row, iterate over the rows and check validity (aka no duplicates)

        # rowSet = set()
        # for row in range(rows):
        #     for col in range(cols):
        #         if board[row][col] == ".":
        #             continue
        #         if board[row][col] in rowSet:
        #             return False
        #         rowSet.add(board[row][col])
        #     rowSet = set()

        # # part 2: determine validity of each col based on above condition
        # # lets creatre a hashset for every col, iterate over the cols and check validity (aka no duplicates)

        # colSet = set()
        # for col in range(cols):
        #     for row in range(rows):
        #         if board[row][col] == ".":
        #             continue
        #         if board[row][col] in colSet:
        #             return False
        #         colSet.add(board[row][col])

        #     colSet = set()

        # # part 3: determine validity of each 3z3 grid
        # # the tricky part here is, given an arbitrary cell, how do we determine which 3x3 grid it belongs to?
        # # eg - row = 4, col = 5
        # # since each grid is 3x3 and there are 9 rows and 9 cols total, lets call the top left grid 0, middle left 1, top right 2, etc
        # # and lets divide the arbitrary row and col by 3 which will give us the new index of the grid
        # # eg - 4/3 = 1, 5/3 = 1
        # # this means we are in the grid (1,1) aka the middle grid
        # # if we create a hashset for each of the 9 grids, we iterate over the board, index into the appropriate subgrid, and determine validity (aka no duplicates)

        # # when indexing intp a random cell, use the following rules:
        # # if row == 0 && col == 0: grid0
        # # if row == 0 && col == 1: grid1
        # # if row == 0 && col == 2: grid2
        # # if row == 1 && col == 0: grid3
        # # if row == 1 && col == 1: grid4
        # # if row == 1 && col == 2: grid5
        # # if row == 2 && col == 0: grid6
        # # if row == 2 && col == 1: grid7
        # # if row == 2 && col == 2: grid8

        # grid0, grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8 = set(), set(), set(), set(), set(), set(), set(), set(), set()

        # for row in range(rows):
        #     for col in range(cols):
        #         if board[row][col] == ".":
        #             continue
        #         gridRow, gridCol = row//3, col//3
        #         if gridRow == 0 and gridCol == 0:
        #             if board[row][col] in grid0:
        #                 print("1")
        #                 return False
        #             grid0.add(board[row][col])
        #         if gridRow == 0 and gridCol == 1:
        #             if board[row][col] in grid1:
        #                 print(grid1)
        #                 return False
        #             grid1.add(board[row][col])
        #         if gridRow == 0 and gridCol == 2:
        #             if board[row][col] in grid2:
        #                 print("3")
        #                 return False
        #             grid2.add(board[row][col])
        #         if gridRow == 1 and gridCol == 0:
        #             if board[row][col] in grid3:
        #                 print("4")
        #                 return False
        #             grid3.add(board[row][col])
        #         if gridRow == 1 and gridCol == 1:
        #             if board[row][col] in grid4:
        #                 print("5")
        #                 return False
        #             grid4.add(board[row][col])
        #         if gridRow == 1 and gridCol == 2:
        #             if board[row][col] in grid5:
        #                 print("6")
        #                 return False
        #             grid5.add(board[row][col])
        #         if gridRow == 2 and gridCol == 0:
        #             if board[row][col] in grid6:
        #                 print("7")
        #                 return False
        #             grid6.add(board[row][col])
        #         if gridRow == 2 and gridCol == 1:
        #             if board[row][col] in grid7:
        #                 print("8")
        #                 return False
        #             grid7.add(board[row][col])
        #         if gridRow == 2 and gridCol == 2:
        #             if board[row][col] in grid8:
        #                 print("9")
        #                 return False
        #             grid8.add(board[row][col])

        # return True

        # now that above solution works and we have the logic down, can we condense the code so its not as verbose?

        # cols is similar to colSet above, except its actually a hashmap where the key is column number and value is a hashset
        cols = collections.defaultdict(set)

        # lets do the same thing for rowSet
        rows = collections.defaultdict(set)

        # lets also do the same thing for grids, where the key is (row//3, col//3), val is hashset
        grids = collections.defaultdict(set)

        # since a sudoku board is 9x9, we can hard code this into our loops
        for r in range(9):
            for c in range(9):
                # start with empty case
                if board[r][c] == ".":
                    continue
                # now we are at the nonempty case
                # we have to now determine which row, col, and grid this specific cell belongs to
                # lets start with row -> we can get that from r
                # col -> we can get that from c
                # grid -> we can get that from r/3, c/3
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in grids[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                grids[(r//3, c//3)].add(board[r][c])

        return True

        # O(n^2) time O(n^2) space

