import random

class Solution:

    def __init__(self, w: List[int]):
        
        self.prefixSums = []
        cumSum = 0
        for weight in w:
            cumSum += weight
            self.prefixSums.append(cumSum)
        self.totalSum = cumSum
            

    def pickIndex(self) -> int:
        
        target = self.totalSum * random.random()
        print(random.random())
        lo, hi = 0, len(self.prefixSums)
        
        while lo < hi:
            mid = (hi + lo) // 2
            if target > self.prefixSums[mid]:
                lo = mid + 1
            else:
                hi = mid
                
        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
