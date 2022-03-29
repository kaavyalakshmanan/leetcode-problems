class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        # O(n) time O(1) space
        # 2 pointers
        
        isDigit = False
        i, j = 0, 0
        
        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                isDigit = False
                if word[i] != abbr[j]:
                    return False
                i+=1
                j+=1
            else:
                if isDigit:
                    return False
                if abbr[j] == '0':
                    return False
                isDigit = True
                digit = ''
                while j < len(abbr) and abbr[j].isdigit():
                    digit += abbr[j]
                    j+=1
                i += int(digit)
                if i > len(word):
                    return False
            
        
        return i == len(word) and j == len(abbr)
