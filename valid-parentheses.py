class Solution:
    def isValid(self, s: str) -> bool:
        
        # O(n) time O(n) space
        # Using a stack
        
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif not stack or ((c == ")" and stack[-1] != "(") or (c == "}" and stack[-1] != "{") or (c == "]" and stack[-1] != "[")):
                return False
            else:
                stack.pop()
            
        return True if not stack else False
