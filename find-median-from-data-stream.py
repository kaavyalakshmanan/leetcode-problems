class MedianFinder:

    def __init__(self):
        # Initialize two heaps: smallHeap (max heap) & largeHeap (min heap)
        # Invariants: 
            # Every element in smallHeap <= every element in largeHeap
            # Lengths of both heaps can differ by at most 1
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # O(logn) time
        # Python implements minHeap but not maxHeap
        # To get around this multiply num by -1
        heapq.heappush(self.small, -1 * num)
        
        # Make sure every element in small <= every element in large
        # Multiply by -1 again to get true value
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 *  heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Make sure length diff is not greater than at most 1
        if len(self.small) > len(self.large) + 1:
            val = -1 *  heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # O(1) time
        if len(self.small) > len(self.large):
            return self.small[0] * -1
            
        if len(self.large) > len(self.small):
            return self.large[0]
        return ((self.small[0] * -1) + self.large[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
