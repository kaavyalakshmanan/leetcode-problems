class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        # O(n*m) time O(n*m) space
        
        ROWS, COLS = len(mat), len(mat[0])
        output = [mat[0][0]]
        row, col = 0, 1
        reverse = False
        
        while col < COLS:
            i, j = row, col
            curr = []
            while i >= 0 and i < ROWS and j >= 0 and j < COLS:
                curr.append(mat[i][j])
                i+=1
                j-=1
            if reverse:
                curr = curr[::-1]
            reverse = not reverse 
            for item in curr:
                output.append(item)
            col+=1
        
        row, col = 1, COLS-1
        while row < ROWS:
            i, j = row, col
            curr = []
            while i >= 0 and i < ROWS and j >= 0 and j < COLS:
                curr.append(mat[i][j])
                i+=1
                j-=1
            if reverse:
                curr = curr[::-1]
            reverse = not reverse 
            for item in curr:
                output.append(item)
            row+=1
        
            
                
        return output 
                
        
            
            
            
