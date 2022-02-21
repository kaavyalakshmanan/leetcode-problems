class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        # O(n) time O(n) space
        
        stack = []
        
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")": 
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack)
        
        # O(n) time O(1) space
        
        ans = bal = 0
        for symbol in s:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal
