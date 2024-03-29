class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # O(nlogk) time O(k) space
        # Max heap
        
        maxHeap = []
        i = 0
        while i < k:
            x, y = points[i][0], points[i][1]
            dist = (x ** 2) + (y ** 2)
            maxHeap.append([dist * -1, x, y])
            i+=1
            
        heapq.heapify(maxHeap)
        
        while i < len(points):
            x, y = points[i][0], points[i][1]
            dist = (x ** 2) + (y ** 2)
            if dist * -1 > maxHeap[0][0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, [dist * -1, x, y])
            i+=1
                
        output = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            output.append([x, y])
            
        return output 
