class Solution:
    def calculate(self, s: str) -> int:
        
        # O(n) time O(n) space 
        # Stack
        
        stack = []
        currDigit, currOp = 0, '+'
        
        def div(num1, num2):
            return int(num1 / num2)
        
        for i, c in enumerate(s):
            if c.isdigit():
                currDigit = (currDigit * 10) + int(c)
            if (not c.isdigit() and not c.isspace()) or i == len(s)-1:
                if currOp == '+':
                    stack.append(currDigit)
                elif currOp == '-':
                    stack.append(-currDigit)
                elif currOp == '*':
                    stack[-1] *= currDigit
                else:
                    stack[-1] = div(stack[-1], currDigit)
                currOp = c
                currDigit = 0
                    
        res = 0
        while stack:
            res += stack.pop()
            
        return res
