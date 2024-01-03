class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # O(n) time O(n) space
        # Sliding window
        
        left, right = 0, 0
        res = 0
        sDict = {}

        while right < len(s):
            if s[right] in sDict and sDict[s[right]] >= left:
                res = max(res, right-left)
                left = sDict[s[right]]+1
            sDict[s[right]] = right
            right+=1

        res = max(res, right-left)
        return res
