class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        # O(n) time O(n) space
        # Using stack
        
        stack = []
        res = 0
        for c in s:
            if c =='(':
                stack.append(c)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack)

        # O(n) time O(1) space
        # Without stack
        
        res, bal = 0, 0
        for c in s:
            bal+=1 if c == '(' else -1
            if bal == -1:
                res+=1
                bal+=1
        return res + bal
