class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # O(n) time O(1) space bc at most 26 chars
        # Sliding window
        
        count = defaultdict(int)
        res, currLen = 0, 0
        left, right = 0, 0

        while right < len(s):
            count[s[right]]+=1
            currLen = max(currLen, count[s[right]])
            if (right-left+1) - currLen > k:
                count[s[left]]-=1
                left+=1
                currLen = max(count.values())
                res = max(res, right-left)
            else:
                res = max(res, right-left+1)
            right+=1

        return res
                

        
