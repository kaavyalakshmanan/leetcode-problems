class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        # obvious brute force -- 3 nested forloops O(n^3)
        # to optimize, look at the constraint --> s consists only of lowercase english letters

        # the idea: iterate over string, treat each char as the middle char in a palindrome
        # since we are only searching for 3 letter palindromes, the outer two characters have to be the same and the middle character can be anything

        # right keeps track of the outer right character used, and it does this by updating this dict which maps character to its count in s
        right = collections.Counter(s)
        # left keeps track of the outer left character used in a set, by adding every unique character seen
        left = set()
        # res contains tuples (middle char, outer char) and its length will be returned
        res = set()

        # iterate over every character, treat as middle
        for c in s:
            # decrement that characters count in right
            # we do this because since we are treating c as middle, we need to decrement its count before using it as outer right
            right[c]-=1

            # if there are no more c's left, pop so we dont use anymore as outer right
            if right[c] == 0:
                right.pop(c)

            # now that we have taken care of middle char, its time to care about outer chars
            # iterate from a to z
            for i in range(26):
                # this is the fancy way of iterating from a-z in python
                currChar = chr(ord('a') + i) 
                if currChar in left and currChar in right:
                    # if we can use currChar as outer left and right, add to result set
                    res.add((c, currChar))

            # also add c to left so we know in the future that c exists
            left.add(c)

        return len(res)

        # this algo is O(26*n) time and O(n) space
