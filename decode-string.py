class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                currStr = ''
                while stack[-1] != '[':
                    currStr = stack.pop() + currStr
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * currStr)
        
        return "".join(stack)
        
