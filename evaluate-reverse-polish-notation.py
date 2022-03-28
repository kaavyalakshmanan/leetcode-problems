class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # O(n) time, O(n) space
        # Use a stack
        
        stack = []
        
        for i, c in enumerate(tokens):
            if len(c) > 1 and c[0] == '-':
                stack.append(-abs(int(c)))
            elif c.isdigit():
                stack.append(int(c))
            else:
                num2, num1 = stack.pop(), stack.pop()
                if c == '+':
                    stack.append(num1 + num2)
                elif c == '-':
                    stack.append(num1 - num2)
                elif c == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
                    
        return stack[0]
                    
        
