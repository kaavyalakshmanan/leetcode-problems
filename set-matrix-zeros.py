class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Approach 1: Use additional space
        # O(n*m) time O(n+m) space
#         rowSet, colSet = set(), set()
#         ROWS, COLS = len(matrix), len(matrix[0])
        
#         for row in range(ROWS):
#             for col in range(COLS):
#                 if matrix[row][col] == 0:
#                     rowSet.add(row)
#                     colSet.add(col)
                    
#         for row in range(ROWS):
#             for col in range(COLS):
#                 if row in rowSet or col in colSet:
#                     matrix[row][col] = 0
                    
        # Approach 2: Without additional space
        # O(m*n) time O(1) space
        
        ROWS, COLS = len(matrix), len(matrix[0])
        # Tells us whether first row is zero
        rowZero = False
        
        # Determine which rows and columns need to be zeroed
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True
                    
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                    
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        
