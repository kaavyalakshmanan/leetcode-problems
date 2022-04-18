class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        # O(n) time O(n) space
        
        citySet = set()
        destCity = ''
        
        for c1, c2 in paths:
            citySet.add(c1)
                
        for c1, c2 in paths:
            if c1 not in citySet:
                return c1
            if c2 not in citySet:
                return c2

      
                
