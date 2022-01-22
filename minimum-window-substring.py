class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # O(n) time O(1) space
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
                
        have, need = 0, len(tDict)
        left, right = 0, 0
        output, length = "", inf
        while right < len(s):
            currChar = s[right]
            if currChar in tDict:
                sDict[currChar]+=1
                if sDict[currChar] == tDict[currChar]:
                    have+=1
            while have == need:
                leftChar = s[left]
                if right-left+1 < length:
                    length = right-left+1
                    output = s[left:right+1]
                if leftChar in sDict:
                    sDict[leftChar]-=1
                    if sDict[leftChar] < tDict[leftChar]:
                        have-=1
                left+=1
            right+=1
                        
        return output 
