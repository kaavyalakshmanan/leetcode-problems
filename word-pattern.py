class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # bijection: single mapping between each character and word
        # O(n) time O(n) space

        s = s.split(" ")
        if len(pattern) != len(s):
            return False

        pDict = {}
        sDict = {}

        for i, c in enumerate(pattern):
            if c not in pDict:
                pDict[c] = s[i]
            elif pDict[c] != s[i]:
                return False

        for i, c in enumerate(s):
            if c not in sDict:
                sDict[c] = pattern[i]
            elif sDict[c] != pattern[i]:
                return False

        return True

