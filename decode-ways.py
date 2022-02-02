class Solution:
    def numDecodings(self, s: str) -> int:
        
        # O(n) time O(1) space
        
        second, third = 1 if s[-1] != "0" else 0, 1
        for i in range(len(s)-2, -1, -1):
            first = 0
            if s[i] != "0":
                currDigit = int(s[i:i+2])
                if currDigit <= 26:
                    first = second + third
                else:
                    first = second
            second, third = first, second
            
        return second
                
