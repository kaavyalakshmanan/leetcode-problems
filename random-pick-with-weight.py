class Solution:

    def __init__(self, w: List[int]):
        
        # O(n) time O(n) space
        # Binary Search
        
        self.prefixSums = []
        self.totalSum = 0
        for weight in w:
            self.totalSum += weight
            self.prefixSums.append(self.totalSum)
        

    def pickIndex(self) -> int:
        
        # O(logn) time O(1) space
        
        target = self.totalSum * random.random()
        l, r = 0, len(self.prefixSums)-1
        
        
        while l <= r:
            m = (l+r)//2
            if self.prefixSums[m] < target:
                l = m + 1
            else:
                r = m - 1 
                
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
