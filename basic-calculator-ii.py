class Solution:
    def calculate(self, s: str) -> int:
        
        # O(n) time O(n) space
        stack = []
        currNum, currChar, op = 0, '', '+'
        length = len(s)
        
        def div(n1, n2):
            if n1 > 0 or n1 % n2 == 0:
                return n1 // n2
            return (n1 // n2) + 1
                
        
        for i in range(length):
            currChar = s[i]
            if currChar.isdigit():
                currNum = (currNum * 10) + int(currChar)
            if (not currChar.isdigit() and not currChar.isspace()) or i == length-1:
                if op == '+':
                    stack.append(currNum)
                elif op == '-':
                    stack.append(-currNum)
                elif op == '*':
                    stack[-1] = stack[-1] * currNum
                else:
                    stack[-1] = div(stack[-1], currNum)
                currNum = 0
                op = currChar
        
        res = 0
        while stack:
            res += stack.pop()
            
        return res
