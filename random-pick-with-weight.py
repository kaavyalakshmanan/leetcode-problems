import random
class Solution:

    def __init__(self, w: List[int]):
        
        self.arr = [0] * len(w)
        totalSum = sum(w)
        for i, num in enumerate(w):
            self.arr[i] = num / totalSum

    def pickIndex(self) -> int:
        
        # O(n) time O(n) space
        # Optimize using binary search O(logn) time O(n) space
              
        randNum = random.uniform(0,1) 
        
        prev = 0
        for i in range(len(self.arr)):
            if randNum >= prev and randNum < self.arr[i] + prev:
                return i
            prev += self.arr[i] 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
