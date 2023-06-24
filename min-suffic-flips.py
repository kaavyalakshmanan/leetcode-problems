class Solution:
    def minFlips(self, target: str) -> int:

        # O(n) time O(1) space
        # prev basically keeps track of what everything in res is after (and including) the index we're in

        numFlips = 0
        prev = '0'

        for num in target:
            if num != prev:
                numFlips += 1
                prev = num

        return numFlips
