class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # O(n) time O(1) space
        # Count array
        
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')]+=1
        for c in t:
            count[ord(c) - ord('a')]-=1
        return True if all(i == 0 for i in count) else False
