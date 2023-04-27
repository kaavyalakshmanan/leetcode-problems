class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # O(n) time O(1) space
        # 2 pointers

        start, end = len(s)-1, len(s)-1

        # Find end pos
        while end >= 0 and not s[end].isalpha():
            end-=1
        
        # Find start pos
        start = end
        while start >= 0 and s[start].isalpha():
            start-=1

        return end-start

       
