class Solution:
    def myPow(self, x: float, n: int) -> float:

        # O(logn) time O(logn) space

        # Base cases
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        def divideAndConquer(x, n):
            # Base case for exo n
            if n == 1:
                return x
            
            val = divideAndConquer(x, n//2)
            val = val * val
            # Odd case
            if n % 2:
                val *= x

            return val

        res = divideAndConquer(x,abs(n)) 
        return res if n > 0 else 1/res
