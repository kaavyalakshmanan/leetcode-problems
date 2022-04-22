class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        subStrs = [""] * len(s)
        lengths = [0] * len(s)
        
        for i in range(len(indices)):
            idx = indices[i]
            lengths[idx] = len(sources[i])
            if s[idx: idx+len(sources[i])] == sources[i]:
                subStrs[idx] = targets[i]
            else:
                subStrs[idx] = s[idx: idx+len(sources[i])]
                
        res = ""
        i = 0
        while i < len(s):
            if not subStrs[i]:
                res += s[i]
                i+=1
            else:
                res += subStrs[i]
                i += lengths[i]
                
        return res
