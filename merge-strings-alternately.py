class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # O(n) time O(n) space
        
        res = ""
        i, j = 0, 0
        k = 0

        while i < len(word1) and j < len(word2):
            if k % 2 == 0:
                res+= word1[i]
                i+=1
            else:
                res += word2[j]
                j+=1
            k+=1

        if i < len(word1):
            res += word1[i:]

        if j < len(word2):
            res += word2[j:]

        return res
