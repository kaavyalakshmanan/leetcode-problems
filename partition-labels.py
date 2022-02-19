class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # O(n) time O(n) space
        # Sliding window
        
        charDict = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in charDict:
                charDict[s[i]] = i
        
        
        left, right = 0, 0
        start = 0
        maxIdx = 0
        output = []
        while right < len(s):
            while left <= right:
                currChar = s[left]
                if charDict[currChar] > maxIdx:
                    maxIdx = charDict[currChar]
                    right = charDict[currChar]
                left+=1
            output.append(right-start+1)
            start = right = right+1
            
        return output 
            
            
        return output 
            
                
            
            
            
