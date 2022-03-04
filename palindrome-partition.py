class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # O(n * 2^n) time O(n) space
        # Backtracking 
        
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        def backtrack(i):
            if i >= len(s):
                output.append(currPart.copy())
                return
        
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    currPart.append(s[i:j+1])
                    backtrack(j+1)
                    currPart.pop()
        
        output = []
        currPart = []
        backtrack(0)
        return output 
