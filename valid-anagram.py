class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # O(n) time O(1) space
        # Frequency counter of chars

        if len(s) != len(t):
            return False

        chars = [0] * 26

        for i in range(len(s)):
            chars[ord(s[i]) - ord('a')]+=1
            chars[ord(t[i]) - ord('a')]-=1

        for c in chars:
            if c != 0:
                return False

        return True


        
