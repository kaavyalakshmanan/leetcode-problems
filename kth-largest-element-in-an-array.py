class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # O(nlogk) time O(k) space
        # Min heap
        
        heap = []
        i = 0
        while i < k:
            heap.append(nums[i])
            i+=1
            
        heapq.heapify(heap)
        
        while i < len(nums):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
            i+=1
        
        return heap[0]
        
        
