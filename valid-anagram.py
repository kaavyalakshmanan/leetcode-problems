class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # O(n) time O(1) space

        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            count[ord(c1)-ord('a')]+=1
            count[ord(c2)-ord('a')]-=1

        for c in count:
            if c != 0:
                return False

        return True
