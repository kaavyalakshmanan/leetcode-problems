class Solution:
    def climbStairs(self, n: int) -> int:
        
        # O(n) time O(n) space
        # Bottom Up DP
        
        cache = [1] * (n+1)
        for i in range(len(cache)-3, -1, -1):
            cache[i] = cache[i+1] + cache[i+2]
            
        return cache[0]
    
        # O(n) time O(1) space
        # Bottom Up DP without extra memory

        first, second = 1, 1
        i = n-2
        while i >= 0:
            curr = first + second
            first, second = curr, first
            i-=1
            
        return first
        
