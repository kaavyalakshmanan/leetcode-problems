class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # O(logn) time O(logn) space
        # D&C
        
        def divideAndConquer(x, n):
            if n == 0:
                return 1
            
            res = divideAndConquer(x, n//2)
            res *= res
            
            return x * res if n % 2 else res
        
            
        
        if x == 0:
            return 0
        
        res = divideAndConquer(x, abs(n))
        return res if n > 0 else 1/res
