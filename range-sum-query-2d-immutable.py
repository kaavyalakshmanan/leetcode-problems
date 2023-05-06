class NumMatrix:

    # O(n*m) time and space to set up constructor

    def __init__(self, matrix: List[List[int]]):

        self.matrix = matrix

        # Step 1: create prefixSum matrix
        # treat each cell as the bottom right corner

        rows, cols = len(matrix), len(matrix[0])
        self.prefixSum = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

        for row in range(rows):
            currSum = 0
            for col in range(cols):
                currSum += matrix[row][col]
                above = self.prefixSum[row][col+1]
                self.prefixSum[row+1][col+1] = currSum + above
        

    # we want this function to be O(1) time and O(1) space
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        bottomRight = self.prefixSum[row2][col2]
        above = self.prefixSum[row1-1][col2]
        left = self.prefixSum[row2][col1-1]
        topLeft = self.prefixSum[row1-1][col1-1]

        return bottomRight - above - left + topLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
