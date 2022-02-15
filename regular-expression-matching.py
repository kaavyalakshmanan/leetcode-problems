class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # O(m*n) time O(m*n) space
        # Memoization
        
        cache = {}
        
        # Backtracking algo with memoization
        def findMatch(i, j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                # Don't use * or use * IF there is match
                cache[(i,j)] = findMatch(i, j+2) or (match and findMatch(i+1, j))
                return cache[(i,j)]
            if match: 
                cache[(i,j)] = findMatch(i+1, j+1)
                return cache[(i,j)]
            else:
                return False
            
        return findMatch(0, 0)
