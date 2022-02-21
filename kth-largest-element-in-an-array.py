class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # O(nlogk) time O(k) space
        # min heap
        
        minHeap = []
        idx = 0
        while idx < k:
            minHeap.append(nums[idx])
            idx+=1
        
        heapq.heapify(minHeap)
        while idx < len(nums):
            if nums[idx] > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[idx])
            idx+=1
                
        return minHeap[0]
