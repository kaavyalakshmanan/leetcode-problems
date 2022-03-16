class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # O(n) time O(1) space
        # 2 pointers
        
        if s == s[::-1]:
            return True
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                removeL = s[:l] + s[l+1:]
                removeR = s[:r] + s[r+1:]
                return removeL == removeL[::-1] or removeR == removeR[::-1]
                
            
        
