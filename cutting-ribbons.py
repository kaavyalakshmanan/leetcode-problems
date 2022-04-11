class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        # O(nlogm) time O(1) space
        l, r = 1, max(ribbons)
        
        def canCutRibbons(length):
            numRibbons = 0
            
            for ribbon in ribbons:
                currLength = ribbon
                numRibbons += currLength // length 
            
            return numRibbons >= k
        
        while l <= r:
            m = (l+r)//2
            
            if canCutRibbons(m):
                l = m + 1
            else:
                r = m - 1
                
        return r
