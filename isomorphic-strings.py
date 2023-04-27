class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # O(n) time O(n) space

        sDict = {}

        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = t[i]
            elif sDict[s[i]] != t[i]:
                return False

        tDict = {}

        for i in range(len(s)):
            if t[i] not in tDict:
                tDict[t[i]] = s[i]
            elif tDict[t[i]] != s[i]:
                return False


        return True


        
