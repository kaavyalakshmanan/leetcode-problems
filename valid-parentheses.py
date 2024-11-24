class Solution:
    def isValid(self, s: str) -> bool:

        # O(n) time O(n) space
        # Use a stack
        
        stack = []
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack) == 0 or (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '[') or (c == '}' and stack[-1] != '{'):
                return False
            else:
                stack.pop()

        return len(stack) == 0
            
