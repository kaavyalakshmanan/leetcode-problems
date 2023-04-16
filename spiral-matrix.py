class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # O(n*m) time O(1) space
        
        res = []
        i, j, ctr = 0, 0, 0
        rows, cols = len(matrix), len(matrix[0])
        total = rows * cols

        while ctr < total:
            # Keep going right
            while j < cols and matrix[i][j] != "":
                res.append(matrix[i][j])
                matrix[i][j] = ""
                j+=1
                ctr+=1
            j-=1
            i+=1
            # Keep going down
            while i < rows and matrix[i][j] != "":
                res.append(matrix[i][j])
                matrix[i][j] = ""
                i+=1
                ctr+=1
            i-=1
            j-=1
            # Keep going left
            while j >= 0 and matrix[i][j] != "":
                res.append(matrix[i][j])
                matrix[i][j] = ""
                j-=1
                ctr+=1
            j+=1
            i-=1
            # Keep going up
            while i >= 0 and matrix[i][j] != "":
                res.append(matrix[i][j])
                matrix[i][j] = ""
                i-=1
                ctr+=1
            i+=1
            j+=1
        
        return res


           

