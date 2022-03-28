class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        # O(n) time O(1) space
        # Iterate forwards and backwards
         
        left, right = 0, 0
        count = 0
        
        for i in range(len(s)):
            currChar = s[i]
            if currChar == "(":
                left+=1
            else:
                right+=1
            if left == right:
                left, right = 0, 0
            if right > left:
                count += 1
                right-=1
        
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            currChar = s[i]
            if currChar == "(":
                left+=1
            else:
                right+=1
            if left == right:
                left, right = 0, 0
            elif left > right:
                count += 1
                left-=1
                
        return count
