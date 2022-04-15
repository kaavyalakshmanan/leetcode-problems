class Solution:
    def checkRecord(self, n: int) -> int:
        
        # O(n) time O(n) space
        
        cache = {}
        MOD = (10**9) + 7
        
        def dfs(n, a, l, p):
            res = 0
            if n == 0:
                return 1
            if (n, l, a) in cache:
                return cache[(n, l, a)]
            
            if a < 1:
                res += dfs(n-1, a+1, 0, p)
            if l < 2:
                res += dfs(n-1, a, l+1, p)
            res += dfs(n-1, a, 0, p)
            
            res %= MOD
            
            cache[(n, l, a)] = res
            
            return cache[(n, l, a)]
        
        return dfs(n, 0, 0, 0)
