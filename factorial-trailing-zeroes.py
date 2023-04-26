class Solution:
    def trailingZeroes(self, n: int) -> int:

        # O(logn) time O(1) space

        if n == 0:
            return 0

        # Step one: use binary search to calculate factorial 
        def calcFactorial(l, r):
            if l == r:
                return l+1

            m = (r+l)//2
            left = calcFactorial(l, m)
            right = calcFactorial(m+1, r)

            return left * right

        fac = calcFactorial(0, n-1)
        lastDigit = fac % 10
        count = 0

        while lastDigit == 0:
            count +=1
            fac = fac // 10
            lastDigit = fac % 10

        return count 


