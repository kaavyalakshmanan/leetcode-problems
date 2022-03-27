class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
#         # O(n) time O(n) space
#         # Use stack
        
        stack = []
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
                    
        output = []
        j = 0
        for i, c in enumerate(s):
            if j < len(stack) and i == stack[j]:
                j+=1
            else:
                output.append(c)
                
        return "".join(output)

        # O(n) time O(1) space
        # Pointers
        
        forwards, backwards = "", ""
        left, right = 0, 0
        
        for i in range(len(s)):
            currChar = s[i]
            if currChar == "(":
                left+=1
            elif currChar == ")":
                right+=1
            if right > left:
                right-=1
            else:
                forwards+=currChar
                
        left, right = 0, 0
        for i in range(len(forwards)-1, -1, -1):
            currChar = forwards[i]
            if currChar == "(":
                left+=1
            elif currChar == ")":
                right+=1
            if left > right:
                left-=1
            else:
                backwards+=currChar
                
        return backwards[::-1]
                
        
            
                
