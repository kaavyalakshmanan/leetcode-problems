class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # O(n) time O(n) space
        # Use a hashmap
        
        charDict = {}
        left, right = 0, 0
        maxLen = 0

        while right < len(s):
            if s[right] in charDict:
                if charDict[s[right]] >= left:
                    left = charDict[s[right]]+1
            maxLen = max(maxLen, right-left+1)
            charDict[s[right]] = right
            right+=1

        return maxLen
