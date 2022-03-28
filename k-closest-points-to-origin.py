class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # O(nlogk) time O(k) space
        # Use max heap
        
        maxHeap = []
        i = 0
        while i < k:
            maxHeap.append([((points[i][0] ** 2) + (points[i][1] ** 2)) * -1, i])
            i+=1
        
        heapq.heapify(maxHeap)
        
        while i < len(points):
            currDist = ((points[i][0] ** 2) + (points[i][1] ** 2)) * -1
            minDist, idx = maxHeap[0]
            if currDist > minDist:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, [currDist, i])
            i+=1
        
        output = []
        for dist, idx in maxHeap:
            output.append(points[idx])
    
        return output 
            
