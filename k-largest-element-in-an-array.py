class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # O(nlogk) time O(logk) space
        # MinHeap
        
        minHeap = []
        i = 0
        
        while i < k:
            minHeap.append(nums[i])
            i+=1
        
        heapq.heapify(minHeap)
        
        while i < len(nums):
            if nums[i] > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])
            i+=1
            
        return minHeap[0]
