class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # O(S*P) time, O(1) space
        # Iterative backtracking 
        
        pIdx, sIdx = 0, 0
        pLen, sLen = len(p), len(s)
        starIdx, sTempIdx = -1, -1
        
        while sIdx < sLen:
            # Case 1: Match
            if pIdx < pLen and p[pIdx] in { s[sIdx], '?' }:
                sIdx+=1
                pIdx+=1
            # Case 2: No match, but '*'
            elif pIdx < pLen and p[pIdx] == '*':
                # Don't take '*'
                starIdx, sTempIdx = pIdx, sIdx
                pIdx+=1
            # Case 3: No match and no '*'
            elif starIdx == -1:
                return False
            # Case 4: No match, but there was a '*' at some point, so backtrack
            else:
                pIdx, sIdx = starIdx+1, sTempIdx+1
                sTempIdx = sIdx
        
        # Return True if remianing in p is all '*', False otherwise
        return all(p[i] == '*' for i in range(pIdx, pLen))
