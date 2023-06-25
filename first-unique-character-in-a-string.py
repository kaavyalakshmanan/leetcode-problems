class Solution:
    def firstUniqChar(self, s: str) -> int:

        # O(n) time O(n) space

        chars = collections.Counter(s)

        for i, c in enumerate(s):
            if chars[c] == 1:
                return i

        return -1
