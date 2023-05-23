class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # O(n) time O(n) space

        left, right = 0, 0
        res = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while right < len(s) and (right-left+1) < k:
            if s[right] in vowels:
                res+=1
            right+=1
        
        currRes = res
        while right < len(s):
            if s[right] in vowels:
                currRes+=1
            res = max(res, currRes)
            if s[left] in vowels:
                currRes-=1
            right+=1
            left+=1

        return res

