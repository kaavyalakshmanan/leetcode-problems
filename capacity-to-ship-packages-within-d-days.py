class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # minWeight, maxWeight
        # O(nlogm) time O(1) space
        l, r = max(weights), sum(weights)
        
        def canShip(targetWeight):
            currWeight = 0
            numDays = 1
            
            for weight in weights:
                currWeight += weight
                if currWeight > targetWeight:
                    numDays += 1
                    currWeight = weight
                    
            return numDays <= days
        
        while l <= r:
            m = (l+r)//2
            
            if canShip(m):
                r = m-1
            else:
                l = m+1
            
        return l    
