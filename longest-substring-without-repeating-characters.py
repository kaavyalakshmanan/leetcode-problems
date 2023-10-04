class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # O(n) time O(n) space
        # Sliding window
        
        res = 0
        currLen = 0
        left, right = 0, 0
        pos = {}

        while right < len(s):
            if s[right] not in pos:
                currLen+=1
                pos[s[right]] = right
            else:
                res = max(res, currLen)
                if pos[s[right]] >= left:
                    left = pos[s[right]]+1
                currLen = (right-left+1)
                pos[s[right]] = right
            right+=1

        return max(res, currLen)
