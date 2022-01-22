class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # O(n) time O(n) space
        # Sliding window
        
        # windowLen - count[char] <= k
        count = {}
        maxCount, length = 0, 0
        left, right = 0, 0
        while right < len(s):
            currChar = s[right]
            count[currChar] = 1 + count.get(currChar, 0)
            maxCount = max(maxCount, count.get(currChar))
            while (right-left+1) - maxCount > k:
                count[s[left]]-=1
                left+=1
                maxCount = max(count.values())
            right+=1
            length = max(length, right-left)
            
        return length
        
            
