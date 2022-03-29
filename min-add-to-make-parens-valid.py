class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        # O(n) time O(1) space
        
        left, right = 0, 0
        count = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                left+=1
            else:
                right +=1
            if right > left:
                count +=1
                left, right = 0, 0
            
        left, right = 0, 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                left+=1
            else:
                right +=1
            if left > right:
                count +=1
                left, right = 0, 0
                
        return count
