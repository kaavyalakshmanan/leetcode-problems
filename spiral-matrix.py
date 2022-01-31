class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # O(m*n) time O(1) space
        output = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            
            # Get every i in top row
            for i in range(left, right):
                output.append(matrix[top][i])
            top+=1
            
            # Get every i in right column
            for i in range(top, bottom):
                output.append(matrix[i][right-1])
            right-=1
            
            if not (left < right and top < bottom):
                break
                
             # Get every i in bottom row
            for i in range(right-1, left-1, -1):
                output.append(matrix[bottom-1][i])
            bottom-=1
            
            # Get every i in left column
            for i in range(bottom-1, top-1, -1):
                output.append(matrix[i][left])
            left+=1
            
        return output 
        
          
