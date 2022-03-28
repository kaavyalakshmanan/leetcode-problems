class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        # O(n) time O(1) space
        # 2 pointers
        
        seenDigit = False
        i, j = 0, 0
        
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                seenDigit = False
                i+=1
                j+=1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                if seenDigit:
                    return False
                seenDigit = True
                idx = ''
                while j < len(abbr) and abbr[j].isdigit():
                    idx += abbr[j]
                    j+=1
                idx = int(idx)
                i += idx
            else:
                return False
                
        return i == len(word) and j == len(abbr)
