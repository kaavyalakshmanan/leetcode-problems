class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # O(n^2) time O(1) space
        
        left, right = 0, len(matrix)-1

        while left < right:
            top, bottom = left, right
            for i in range(right-left):
                # Save topLeft
                topLeft = matrix[top][left+i]
                # Move bottomLeft into topLeft
                matrix[top][left+i] = matrix[bottom-i][left]
                # Move bottomRight into bottomLeft
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # Move topRight into bottomRight
                matrix[bottom][right-i] = matrix[top+i][right]
                # Move topLeft into topRight
                matrix[top+i][right] = topLeft
            left+=1
            right-=1


