class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # O(n*m) time O(1) space
        
        lcp = ""
        minLen = inf

        for s in strs:
            if len(s) < minLen:
                lcp = s
                minLen = len(s)

        for s in strs:
            i = 0
            while i < len(lcp) and s[i] == lcp[i]:
                i+=1
            lcp = lcp[:i]

        return lcp
                
