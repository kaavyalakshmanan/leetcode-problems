class Solution:
    def climbStairs(self, n: int) -> int:

        # O(n) time O(1) space

        if n == 1:
            return 1
        if n == 2:
            return 2

        first, second = 2, 1
        i = 2

        while i < n:
            temp = first
            first += second
            second = temp
            i+=1
        
        return first
