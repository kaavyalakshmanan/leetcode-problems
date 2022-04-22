class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        # O(n) time O(n) space
        
        arr = sentence.split(" ")
        length = len(searchWord)
        
        for i, word in enumerate(arr):
            if length-1 < len(word) and word[:length] == searchWord:
                return i+1
            
        return -1
