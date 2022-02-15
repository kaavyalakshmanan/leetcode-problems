class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        # O(n) time O(1) space
        
        numOpen, numClose = 0, 0
        longest = 0
        for i in range(len(s)):
            currChar = s[i]
            if currChar == "(":
                numOpen+=1
            else:
                numClose+=1
            if numOpen == numClose:
                longest = max(2 * numClose, longest)
            elif numClose > numOpen:
                numOpen = numClose = 0
                
        numOpen = numClose = 0
        for i in range(len(s)-1, -1, -1):
            currChar = s[i]
            if currChar == "(":
                numOpen+=1
            else:
                numClose+=1
            if numOpen == numClose:
                longest = max(longest, (2*numOpen))
            elif numOpen > numClose:
                numOpen = numClose = 0
                
        return longest
           
            
