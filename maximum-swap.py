class Solution:
    def maximumSwap(self, num: int) -> int:
        
        # O(n^2) time worst case O(n) space
        
        numsCopy = list(str(num))
        # Map digit to its last seen idx from left to right
        digitsMap = { dig: idx for idx, dig in enumerate(numsCopy) }
        
        for idx, char in enumerate(numsCopy):
            for j in range(9, int(char), -1):
                d = str(j)
                if d in digitsMap and digitsMap[d] > idx:
                    numsCopy[idx], numsCopy[digitsMap[d]] = numsCopy[digitsMap[d]], numsCopy[idx]
                    return int("".join(numsCopy))
                
        return num
                    
                    
            
            
