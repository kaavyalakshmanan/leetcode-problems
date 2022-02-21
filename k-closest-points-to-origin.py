import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # O(nlogk) time O(n) space
        # Use a minHeap
        
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
            
        heapq.heapify(minHeap)
        output = []
        
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            output.append([x, y])
            k-=1
            
        return output 

        O(nlogk) time O(k) space
        Use a max heap with space optimization
        
        maxHeap = []
        idx = 0
        
        while idx < k:
            x, y = points[idx][0], points[idx][1]
            dist = (x ** 2) + (y ** 2)
            maxHeap.append([dist * -1, x, y])
            idx+=1
        
        heapq.heapify(maxHeap)
        output = []
        
        while idx < len(points):
            x, y = points[idx][0], points[idx][1]
            dist = (x ** 2) + (y ** 2)
            prevDist = maxHeap[0][0]
            if (dist * -1) > prevDist:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, [dist * -1, x, y])
            idx+=1
        
        while len(maxHeap) > 0:
            output.append([maxHeap[0][1], maxHeap[0][2]])
            heapq.heappop(maxHeap)
                
        return output

        # O(n) time O(n) space
        # Binary Search
        
        # Precompute the Euclidean distance for each point
        distances = [self.euclidean_distance(point) for point in points]
        # Create a reference list of point indices
        remaining = [i for i in range(len(points))]
        # Define the initial binary search range
        low, high = 0, max(distances)
        
        # Perform a binary search of the distances
        # to find the k closest points
        closest = []
        while k:
            mid = (low + high) / 2
            closer, farther = self.split_distances(remaining, distances, mid)
            if len(closer) > k:
                # If more than k points are in the closer distances
                # then discard the farther points and continue
                remaining = closer
                high = mid
            else:
                # Add the closer points to the answer array and keep
                # searching the farther distances for the remaining points
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                low = mid
                
        # Return the k closest points using the reference indices
        return [points[i] for i in closest]

    def split_distances(self, remaining: List[int], distances: List[float],
                        mid: int) -> List[List[int]]:
        """Split the distances around the midpoint
        and return them in separate lists."""
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid:
                closer.append(index)
            else:
                farther.append(index)
        return [closer, farther]

    def euclidean_distance(self, point: List[int]) -> float:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2
        
                
