class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        # O(n*m) time O(1) space
        
        i, j = 0, 0
        while j < len(abbr):
            currChar = ''
            while j < len(abbr) and abbr[j].isnumeric():
                currChar += abbr[j]
                j+=1
            if currChar:
                if currChar[0] == '0':
                    return False
                currIdx = int(currChar)
                if i + currIdx <= len(word):
                    i += currIdx
                else:
                    return False
            if i < len(word) and j < len(abbr) and abbr[j] != word[i]:
                return False
            if i >= len(word) and j < len(abbr):
                return False
            if i < len(word) and j >= len(abbr):
                return False
            i+=1
            j+=1
                
                
        return j >= len(abbr) and i >= len(word)
            
        
