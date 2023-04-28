class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        # we are given a word (text) and we want to return the number of times we can rearrange the letters in text to form the word "balloon"
        # the way to do this is by computing the number of times b, a, l, o, and n appear in text
        # divide that by the number of times those letters appear in balloon to get the ratio
        # then take the min of the ratios which will give us the bottleneck

        # O(n) time O(1) space

        count = {
            'b': [0, 1],
            'a': [0, 1],
            'l': [0, 2],
            'o': [0, 2],
            'n': [0, 1]
        }

        for c in text:
            if c in count:
                count[c][0]+=1

        minCount = inf
        for k in count:
            v = count[k]
            minCount = min(minCount, v[0]//v[1])

        return minCount

            

