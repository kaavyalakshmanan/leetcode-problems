class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # O(n^2*m) time O(n) space
        # Bottom Up DP
        
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        
        for i in range(len(dp)-2, -1, -1):
            for word in wordDict:
                if i + len(word) < len(dp) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+ len(word)]
                    if dp[i] == True:
                        break
        return dp[0]
