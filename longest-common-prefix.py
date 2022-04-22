class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # O(m*n) time O(n) space
        
        prevLCP = strs[0]
        
        for i in range(1, len(strs)):
            currLCP = ""
            word1 = prevLCP
            word2 = strs[i]
            
            length = min(len(word1), len(word2))
            j = 0
            while j < length and word1[j] == word2[j]:
                currLCP += word1[j]
                j+=1
            prevLCP = currLCP
            
        return prevLCP
                
                
            
            
