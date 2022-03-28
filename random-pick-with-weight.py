class Solution:
    

    def __init__(self, w: List[int]):
        # O(n) time O(n) space
        
        self.prefixSums = []
        cumSum = 0
        for weight in w:
            cumSum += weight
            self.prefixSums.append(cumSum)
            
        self.totalSum = cumSum
            
        
        

    def pickIndex(self) -> int:
        
        # O(logn) time O(1) space
        
        target = random.random() * self.totalSum
        prev = 0
        l, r = 0, len(self.prefixSums)-1
        
        while l <= r:
            m = (r+l)//2
            if target > self.prefixSums[m]:
                l = m+1
            elif target < self.prefixSums[m]:
                r = m-1
                
        return l
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
