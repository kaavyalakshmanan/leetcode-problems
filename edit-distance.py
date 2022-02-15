class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # O(m*n) time O(m) space
        # Bottom Up DP
        
        ROWS, COLS = (len(word2)), (len(word1))
        
        prevRow = [ i for i in range(COLS, -1, -1) ]
        
        for row in range(ROWS-1, -1, -1):
            currRow = [0] * len(prevRow)
            for col in range(COLS, -1, -1):
                if col == COLS:
                    currRow[col] = prevRow[col] + 1
                else:
                    if word2[row] == word1[col]:
                        currRow[col] = prevRow[col+1]
                    else:
                        currRow[col] =  1 + min(currRow[col+1], prevRow[col], prevRow[col+1]) 
                        
            prevRow = currRow
            
        return prevRow[0]
                
