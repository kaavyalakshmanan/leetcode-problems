class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # O(n^2) time O(1) space
        # Expand around center 

        maxLen, left, right = 0, 0, 0
        
        for i in range(len(s)):
            evenLen, evenLeft, evenRight = self.findLongest(i, i+1, s)
            oddLen, oddLeft, oddRight = self.findLongest(i, i, s)

            if evenLen > maxLen and evenLen > oddLen:
                maxLen = evenLen
                left, right = evenLeft, evenRight
            elif oddLen > maxLen and oddLen > evenLen:
                maxLen = oddLen
                left, right = oddLeft, oddRight

        return s[left+1:right]

    def findLongest(self, left: int, right: int, s: str) -> (int, int, int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return (right-left-1, left, right)
        
