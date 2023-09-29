class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # O(n*m) time O(n*m) space
        # HashSet

        rowsSet, colsSet, subSet = defaultdict(set), defaultdict(set), defaultdict(set)
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == ".":
                    continue
                currNum = int(board[row][col])
                if currNum in rowsSet[row] or currNum in colsSet[col] or currNum in subSet[(row//3, col//3)]:
                    return False
                rowsSet[row].add(currNum)
                colsSet[col].add(currNum)
                subSet[(row//3, col//3)].add(currNum)

        return True

        
        
