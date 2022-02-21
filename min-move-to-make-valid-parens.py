class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # O(n) time O(n) space
        # Using a stack
        
#         output = ""
#         stack = []
        
#         for i in range(len(s)):
#             currChar = s[i]
#             if currChar == "(":
#                 stack.append(i)
#             elif currChar == ")":
#                 if stack and s[stack[-1]] == "(":
#                     stack.pop()
#                 else:
#                     stack.append(i)
        
#         stackSet = set(stack)
#         for i in range(len(s)):
#             if i not in stackSet:
#                 output += s[i]
                
#         return output 
    
        # O(n) time O(1) space
        # 2 passes
        
        forwards = ""
        backwards = ""
        numLeft, numRight = 0, 0
        i = 0
        while i < len(s):
            currChar = s[i]
            if currChar == "(":
                numLeft+=1
            elif currChar == ")":
                numRight+=1
            if numRight > numLeft:
                numRight-=1
            else:
                forwards+=currChar
            i+=1
        
        numLeft, numRight = 0, 0
        i = len(forwards)-1
        while i >= 0:
            currChar = forwards[i]
            if currChar == "(":
                numLeft+=1
            elif currChar == ")":
                numRight+=1
            if numLeft > numRight:
                numLeft-=1
            else:
                backwards+=currChar
            i-=1
                
        return backwards[::-1]
        
        
