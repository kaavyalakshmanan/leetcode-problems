class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        # O(n) time O(1) space

        numCapitals = 0
        
        for i, c in enumerate(word):
            if c.isupper():
                numCapitals+=1
                if numCapitals == 1 and i > 0:
                    return False
            

        return numCapitals == 0 or numCapitals == len(word) or numCapitals == 1
