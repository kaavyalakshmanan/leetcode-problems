class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # O(n*m) time O(n) space
        # Bottom Up DP
        
        prevRow = [0] * (len(text1)+1)
        
        for i in range(len(text2)-1, -1, -1):
            currRow = [0] * (len(text1)+1)
            for j in range(len(currRow)-2, -1, -1):
                if text1[j] == text2[i]:
                    currRow[j] = 1 + prevRow[j+1]
                else:
                    currRow[j] = max(currRow[j+1], prevRow[j])
            prevRow = currRow
            
        return prevRow[0]
