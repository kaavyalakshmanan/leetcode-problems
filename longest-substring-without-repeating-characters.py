class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # O(n) time O(n) space
        # Sliding window
        
        charDict = {}
        left, right = 0, 0
        length = 0
        while right < len(s):
            if s[right] not in charDict:
                length = max(length, right-left+1)
            elif charDict[s[right]] >= left:
                left = charDict[s[right]] + 1
                length = max(length, right-left)
            else:
                length = max(length, right-left+1)  
            charDict[s[right]] = right
            right+=1
            
        return length
