class Solution:
    def validPalindrome(self, s: str) -> bool:

        # O(2n) time worst case, O(n) space

        left, right = 0, len(s)-1
        numModifications = 0
        while left < right:
            if s[left] != s[right]:
                skipL, skipR = s[:left] + s[left+1:], s[:right] + s[right+1:]
                if skipL == skipL[::-1] or skipR == skipR[::-1]:
                    return True
                return False
            else:
                left+=1
                right-=1

        return True

