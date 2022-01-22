class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # O(n) time O(n) space
        # Sliding window
        
        charDict = {}
        left, right = 0, 0
        length = 0
        while right < len(s):
            currChar = s[right]
            if currChar not in charDict:
                length = max(length, right-left+1)
            elif charDict.get(currChar) >= left:
                left = charDict.get(currChar) + 1
                length = max(length, right-left)
            else:
                length = max(length, right-left+1)
            charDict[currChar] = right
            right+=1
            
        return length
