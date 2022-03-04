class Solution:
    def numTrees(self, n: int) -> int:
        
        # O(n^2) time O(n) space
        # DP
        
        dp = [1] * (n + 1)
        # dp[0] = 1 --> empty tree
        # dp[1] = 1 --> 1 node
        
        for nodes in range(2, n+1):
            # Consider each i as a root
            total = 0
            for root in range(1, nodes+1):
                left = root - 1
                right = nodes - root
                total += (dp[left] * dp[right])
            dp[nodes] = total
            
        return dp[n]
