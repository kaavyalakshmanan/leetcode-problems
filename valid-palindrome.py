class Solution:
    def isPalindrome(self, s: str) -> bool:

        # O(n) time O(1) space
        # 2 pointers

        left, right = 0, len(s)-1
        while left <= right:
            while left <= right and not s[left].isalnum():
                left+=1
            while right >= left and not s[right].isalnum():
                right-=1
            if left > right:
                return True
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1

        return True
