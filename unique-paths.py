class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Bottom Up DP
        # O(m*n) time O(n) space

        prevRow = [1] * n
        i = 0
        
        while i < m-1:
            currRow = [1] * n
            for j in range(len(currRow)-2, -1, -1):
                currRow[j] = currRow[j+1] + prevRow[j]
            prevRow = currRow
            i+=1

        return prevRow[0]
