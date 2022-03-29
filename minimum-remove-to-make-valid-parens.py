class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # O(n) time O(n) space
        
        left, right = 0, 0
        forwards = ""
        
        for i in range(len(s)):
            if s[i] == "(":
                left+=1
            elif s[i] == ")":
                right+=1
            if right <= left:
                forwards += s[i]
            else:
                left, right, = 0, 0
        
        left, right = 0, 0 
        backwards = ""
        for i in range(len(forwards)-1, -1, -1):
            if forwards[i] == "(":
                left+=1
            elif forwards[i] == ")":
                right+=1
            if left <= right:
                backwards += forwards[i]
            else:
                left, right, = 0, 0
        
        return backwards[::-1]
        
                
