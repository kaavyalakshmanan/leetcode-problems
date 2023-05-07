class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # given a string consisting of uppercase english characters, return the length of the longest substring with the same character if we can make at most k changes
        # the general idea: windowLength - count[mostFreqCharacter] <= k
        # so lets make use of a count dict and sliding window technique

        # O(n) time O(n) space

        left, right = 0, 0
        count = defaultdict(int)
        res, mostFreq = 0, 0

        while right < len(s):
            count[s[right]]+=1
            mostFreq = max(mostFreq, count[s[right]])
            currLen = right-left+1
            if currLen - mostFreq <= k:
                res = max(res, currLen)
            else:
                count[s[left]]-=1
                mostFreq = max(count.values())
                left+=1
            right+=1

        return res
