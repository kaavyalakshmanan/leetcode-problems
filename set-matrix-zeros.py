class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # O(n*m) time O(n+m) space

        rowSet, colSet = set(), set()
        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rowSet.add(row)
                    colSet.add(col)

        for row in range(rows):
            for col in range(cols):
                if row in rowSet or col in colSet:
                    matrix[row][col] = 0

        # We can optimize on this solution by using O(1) memory

        # rowZero is going to indicate whether the 0th row needs to be 0's
        rowZero = False
        rows, cols = len(matrix), len(matrix[0])

        # Step 1: Indicate in the matrix what rows and cols need to be 0
        # The way to do this is to iterate over matrix, if we encounter a 0, set the corresponding start of that column to 0
        # If the current row we're in is 0, set rowZero to True, otherwise set the corresponding start of that row to 0
        # The reason we do this is because matrix[0][0] being 0 means entire 0th column needs to be 0's
        # Whereas rowZero being True means entire 0th row needs to be 0's

        for row in range(rows):
            for col in range(cols):
                # We encountered a 0
                if matrix[row][col] == 0:
                    # Mark corresponding start of this column as 0
                    matrix[0][col] = 0
                    # We only do the same thing for row if currRow > 0
                    # So lets first check that
                    if row > 0:
                        matrix[row][0] = 0
                    # Otherwise, set rowZero to True
                    else:
                        rowZero = True

        # Step 2: Iterate over matrix again, this time staring at row = 1, col = 1 position
        # We check if that cell's corresponding 0th row or col is 0, if so set this cell to 0
        # Its important to note that we start at matrix[1][1], meaning this iteration does not care about 0th row or 0th col
        # Thats because we handle those as separate cases later
        for row in range(1, rows):
            for col in range(1, cols):
                # Check corresponding 0th row and 0th col
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        # Step 3: Handle the 0th col case
        # For this, we check if matrix[0][0] == 0, if so set the 0th col to 0's
        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0

        # Step 4: handle the 0th row case
        # For this, check the value of rowZero
        if rowZero:
            for col in range(cols):
                matrix[0][col] = 0

        # this whole algorithm is still O(n*m) time, but now its O(1) space


        




        
