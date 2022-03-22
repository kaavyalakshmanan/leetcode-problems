class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # O(logn) time O(logn) space
        # Divide and Conquer
        
        if x == 0:
            return 0
        
        def recursiveHelper(n):
    
            if n == 0:
                return 1
            
            res = recursiveHelper(n // 2)
            res *= res
            
            return res * x if n % 2 else res
        
        res = recursiveHelper(abs(n)) 
        return res if n >= 0 else 1 / res
