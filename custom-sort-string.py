class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        # O(max(m,n)) time O(n) space
        
        output = ""
        sDict = {}
        for c in s:
            sDict[c] = 1 + sDict.get(c, 0)
        
        for c in order:
            if c in sDict:
                while sDict[c] > 0:
                    output+=c
                    sDict[c]-=1
        
        for key, val in sDict.items():
            currVal = val
            while currVal > 0:
                output+=key
                currVal-=1
                
        return output 
