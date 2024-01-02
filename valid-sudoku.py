class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # O(1) time O(1) space
        # Use hash set
        
        rowsSet, colsSet, subSet = defaultdict(set), defaultdict(set), defaultdict(set)
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                currVal = board[row][col]
                if currVal == ".":
                    continue
                if currVal in rowsSet[row] or currVal in colsSet[col] or currVal in subSet[(row//3, col//3)]:
                    return False
                rowsSet[row].add(currVal)
                colsSet[col].add(currVal)
                subSet[(row//3, col//3)].add(currVal)

        return True
                
