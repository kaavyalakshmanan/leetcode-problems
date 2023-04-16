class Solution:
    def isValid(self, s: str) -> bool:

        # O(n) time O(n) space
        
        # Stack will keep track of open brackets seen so far
        # We pop from stack when we see corresponding close bracket 
        stack = []

        for c in s:
            # Open bracket case
            if c in {'(', '[', '{'}:
                stack.append(c)
            # Close bracket case
            else:
                # Haven't seen a corresponding open bracket
                if len(stack) == 0:
                    return False
                # Mismatch case
                if (c == ')' and stack[-1] != "(") or (c == ']' and stack[-1] != "[") or (c == '}' and stack[-1] != "{"):
                    return False

                stack.pop()

        return len(stack) == 0
