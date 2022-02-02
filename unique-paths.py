class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # O(m*n) time O(n) space
        # Bottom Up DP
        
        if m == 1 and n == 1:
            return 1
        
        prevRow = [1] * n
        prevRow[-1] = 0
        
        for i in range(m-2, -1, -1):
            currRow = [1] * n
            for j in range(n-2, -1, -1):
                currRow[j] = currRow[j+1] + prevRow[j]
            prevRow = currRow
            
        return prevRow[0]
