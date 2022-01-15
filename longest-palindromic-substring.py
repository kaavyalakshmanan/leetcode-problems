class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # O(n^2) time O(1) space
        # Expand around center
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return right-left-1
        
        start, end = 0, 0
        for i in range(len(s)):
            oddLen = expandAroundCenter(i, i)
            evenLen = expandAroundCenter(i, i+1)
            maxLen = max(oddLen, evenLen)
            
            if maxLen > end-start:
                start = i - (maxLen-1)//2
                end = i + (maxLen//2)
                
        return s[start:end+1]
