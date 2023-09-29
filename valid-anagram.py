class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # O(n) time O(1) space
        # Frequency count
        
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i, c in enumerate(s):
            count[ord(c) - ord('a')]+=1
            count[ord(t[i]) - ord('a')]-=1
        
        for c in count:
            if c != 0:
                return False

        return True
