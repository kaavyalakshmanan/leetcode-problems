class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # O(n^2*m) time O(n) space

        dp = [False] * (len(s)+1)
        dp[len(dp)-1] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)-1) < len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                    if dp[i]:
                        break

        return dp[0]
                

