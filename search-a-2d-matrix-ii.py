class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Pruning
        # O(n*m) time O(1) space
        row, col = len(matrix)-1, 0
        cols = len(matrix[0])
        
        while row >= 0 and col < cols:
            if matrix[row][col] > target:
                row-=1
            elif matrix[row][col] < target:
                col+=1
            else:
                return True

        return False


