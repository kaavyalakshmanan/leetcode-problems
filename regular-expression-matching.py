class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # O(s*p) time O(s*p) space
        # Top down memoization
        
        def findMatch(i, j):
            # Base cases
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i,j) in cache:
                return cache[(i,j)] 

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                # Use star or don't use star
                # If we are using star, there has to be a match
                cache[(i,j)] = (match and findMatch(i+1, j)) or findMatch(i, j+2)
                return cache[(i,j)] 
            if match: 
                cache[(i,j)] = findMatch(i+1, j+1)
                return cache[(i,j)] 
            else:
                cache[(i,j)] = False
                return cache[(i,j)] 
            
        cache = {}
        return findMatch(0, 0)
