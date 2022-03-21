class Solution:
    def calculate(self, s: str) -> int:
        
        # O(n) time O(n) space
        
        stack = []
        currDigit, currChar, currOp = 0, '', '+'
        length = len(s)
        
        def div(n1, n2):
            if n1 > 0 or n1 % n2 == 0:
                return n1 // n2
            return (n1 // n2) + 1
        
        for i in range(length):
            currChar = s[i]
            if currChar.isdigit():
                currDigit = (currDigit * 10) + int(currChar)
            if (not currChar.isdigit() and not currChar.isspace()) or i == length-1:
                if currOp == '+':
                    stack.append(currDigit)
                elif currOp == '-':
                    stack.append(-currDigit)
                elif currOp == '*':
                    stack[-1] = stack[-1] * currDigit
                else:
                    stack[-1] = div(stack[-1], currDigit)
                currDigit = 0
                currOp = currChar
        
        res = 0
        while stack:
            res += stack.pop()
            
        return res
            
