class Solution:
    def isValid(self, s: str) -> bool:

        # O(n) time O(n) space
        # Use a stack
        
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif stack:
                if (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '[') or (c == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
            else:
                return False

        return not stack
