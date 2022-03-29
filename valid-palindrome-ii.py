class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # O(n) time O(1) space
        # 2 pointers 
        
        if s == s[::-1]:
            return True
        
        left, right = 0, len(s)-1
        
        while left <= right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                removeLeft = s[:left] + s[left+1:]
                removeRight = s[:right] + s[right+1:]
                
                return removeLeft == removeLeft[::-1] or removeRight == removeRight[::-1]
