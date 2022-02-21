class Solution:
    def calculate(self, s: str) -> int:
        
        length = len(s)
        stack = []
        currNum, op = 0, '+'
        
        for i in range(length):
            currChar = s[i]
            if currChar.isdigit():
                currNum = (currNum * 10) + (currChar - '0')
            if (not currChar.isDigit() and not currChar.isspace()) or i == length - 1:
                if op == '-':
                    stack.push(-currNum)
                elif op == '+':
                    stack.push(currNum)
                elif op == '*':
                    stack.push(stack.pop() * currNum)
                elif op == '/':
                    stack.push(stack.pop() / currNum)
                op = currChar
                currNum = 0
                
        res = 0
        while stack:
            res += stack.pop()
            
        return res
