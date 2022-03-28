class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # O(logn) time O(logn) space
        # Divide and Conquer
        
        def recursiveHelper(x, n):
            if n == 0:
                return 1

            res = self.myPow(x, n//2)
            res *= res
            if n % 2 == 1:
                res *= x

            return res
        
        if x == 0:
            return 0
        
        
        res = recursiveHelper(x, abs(n)) 
        return 1/res if n < 0 else res
