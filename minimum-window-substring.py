class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # O(n+m) time O(n+m) space
        # Sliding window
        
        if len(t) > len(s):
            return ""

        sDict, tDict = {}, {}
        for c in t:
            if c not in tDict:
                tDict[c] = 1
                sDict[c] = 0
            else:
                tDict[c]+=1

        have, need = 0, len(sDict)
        left, right = 0, 0
        start, end = -1, -1
        res = inf

        while right < len(s):
            if s[right] in sDict:
                sDict[s[right]]+=1
                if sDict[s[right]] == tDict[s[right]]:
                    have+=1
                while have == need:
                    if right-left+1 < res:
                        start, end = left, right 
                        res = right-left+1
                    if s[left] in sDict:
                        sDict[s[left]]-=1
                        if sDict[s[left]] < tDict[s[left]]:
                            have-=1
                    left+=1
            right+=1

        return s[start: end+1]
            
