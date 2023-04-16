class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # We are going to use backtracking to solve this
        # We will memoize with a cache to make more efficient
        # O(n*m) time O(n*m) space because of memoization
        # Would have been O(2^n) time if we just did backtracking without memoization


        cache = {}

        def backtracking(i, j):
            # Base case already in cache
            if (i,j) in cache:
                return cache[(i,j)]

            # Base case True case
            if i == len(s) and j == len(p):
                return True
            
            # Base case False case
            if j == len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # * case
            if j+1 < len(p) and p[j+1] == "*":
                # Take * if match or don't take *
                cache[(i,j)] = (match and backtracking(i+1, j)) or backtracking(i, j+2)
                return cache[(i,j)]
            # Match case
            if match:
                cache[(i,j)] = backtracking(i+1, j+1)
                return cache[(i,j)]
            # False case
            else:
                cache[(i,j)] = False
                return cache[(i,j)]

        return backtracking(0, 0)
