class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # O(n) time O(m) space
        # Sliding window
        
        if len(s) < len(p):
            return []
        
        pDict, sDict = {}, {}
        output = []
        for c in p:
            pDict[c] = 1 + pDict.get(c, 0)
            sDict[c] = 0 + sDict.get(c, 0)
            
        have, need = 0, len(pDict)
        left, right = 0, 0
        
        # Move right ptr to correct window length
        while right-left+1 < len(p):
            if s[right] in sDict:
                sDict[s[right]]+=1
                if pDict[s[right]] == sDict[s[right]]:
                    have+=1
            right+=1
                  
        while right < len(s):
            if s[right] in sDict:
                sDict[s[right]]+=1
                if pDict[s[right]] == sDict[s[right]]:
                    have+=1
                if have == need:
                    output.append(left)
            if s[left] in sDict:
                if sDict[s[left]] == pDict[s[left]]:
                    have-=1
                sDict[s[left]]-=1
            left+=1
            right+=1
            
        return output
