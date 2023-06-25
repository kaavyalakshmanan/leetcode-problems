class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        # given a binary string, what is the min number of flips to make it monotone increasing?
        # monotone increasing means the string consists of 0 or more 0s and 0 or more 1s, but all the 0s are on the left side and all the 1s are on the right side
        # a flip means we flip 0 to 1 and vice versa

        # the naive approach would be a backtraking algorithm where for every position, we could try 0 and 1 and see which gives us monotone increasing with minimum number of flips
        # however it's possible to solve this in linear algo

        # s = "010110"
        # iterate over string, keep track of countOne (which counts all 1s seen so far) and res (which is what we will return), both initialized to 0
        # for every 0, take the minimum of countOne and res+1, which is what res will be
        # for every 1, increment countOne
        # return res

        # O(n) time O(1) space

        countOne, res = 0, 0
        for c in s:
            if c == "0":
                res = min(countOne, res+1)
            else:
                countOne+=1

        return res
