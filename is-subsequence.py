class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # O(m+n) time O(1) space where n = len(s) and m = len(t)

        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        p1, p2 = 0, 0

        while p1 < len(s):
            if s[p1] == t[p2]:
                p1+=1
                p2+=1
            else:
                p2+=1
            if p2 == len(t) and p1 < len(s):
                return False

        return True
