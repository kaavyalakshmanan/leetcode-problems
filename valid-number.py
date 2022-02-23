class Solution:
    def isNumber(self, s: str) -> bool:
        
        # O(n) time O(n) space
        
        seenDigit = seenExponent = seenDot = False
        
        for i, c in enumerate(s):
            # c is a digit
            if c.isdigit():
                seenDigit = True
            # c is a sign
            elif c in {'-', '+'}:
                if i > 0 and s[i-1] not in {'e', 'E'}:
                    return False
            elif c in {'e', 'E'}:
                if seenExponent or not seenDigit:
                    return False
                seenExponent = True
                seenDigit = False
            elif c == '.':
                if seenDot or seenExponent:
                    return False
                seenDot = True
            else:
                return False
            
        return seenDigit
                
                
                
                
            
        
