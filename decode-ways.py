class Solution:
    def numDecodings(self, s: str) -> int:

        # O(n) tiem O(n) space
        # Memoization

        cache = { len(s): 1 }

        def backtrack(idx):

            if idx in cache:
                return cache[idx]

            if s[idx] == "0":
                return 0

            res = backtrack(idx+1)

            if idx+1 < len(s) and (s[idx] == "1" or (s[idx] == "2" and s[idx+1] in "0123456")):
                res+=backtrack(idx+2)

            cache[idx] = res

            return res

        return backtrack(0)
