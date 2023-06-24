class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # we can use LCS algo to solve this problem
        # text1 = s text2 = s[::-1]
        # O(n^2) time O(n) space

        prev = [0 for i in range(len(s)+1)]

        for i in range(len(s)):
            curr = [0 for k in range(len(s)+1)]
            for j in range(len(s)-1, -1, -1):
                if s[i] == s[j]:
                    curr[j] = prev[j+1] + 1
                else:
                    curr[j] = max(curr[j+1], prev[j])

            prev = curr

        return prev[0]
