class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, right = 0, 0
        count = defaultdict(int)
        maxCount = 0
        res, currLen = 0, 0

        while right < len(s):
            count[s[right]]+=1
            maxCount = max(maxCount, count[s[right]])
            if (right-left+1) - maxCount <= k:
                res = max(res, right-left+1)
                right+=1
            else:
                while (right-left+1) - maxCount > k:
                    count[s[left]]-=1
                    left-=1
                    maxCount = max(count.values())

        return res
