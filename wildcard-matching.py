class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # O(min(s,p)) time O(1) space
        # Iterative Backtracking
        
        starIdx, sTempIdx = -1, -1
        i, j = 0, 0

        while i < len(s):
            # Match case
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i, j = i+1, j+1
            # * case
            elif j < len(p) and p[j] == '*':
                starIdx = j
                sTempIdx = i
                # Dont take *
                j+=1
            elif starIdx != -1:
                # Take *
                j = starIdx
                i = sTempIdx+1
            else:
                return False

        return all(p[x] == "*" for x in range(j, len(p)))
