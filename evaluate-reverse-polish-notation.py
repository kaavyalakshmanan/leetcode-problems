class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # O(n) time O(n) space
        
        stack = []
        
        for c in tokens:
            if c.isdigit():
                stack.append(int(c))
            elif c[1:].isdigit():
                
                stack.append(int(c[1:]) * -1)
            else:
                second = stack.pop()
                first = stack.pop()
                if c == '+':
                    stack.append(first + second)
                elif c == '-':
                    stack.append(first - second)
                elif c == '*':
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
                    
        res = 0
        while stack:
            res += stack.pop()
            
        return res
        
                    
