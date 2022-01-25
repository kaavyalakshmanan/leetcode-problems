class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # O(n) time O(n) space
        # Bucket Sort
        
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        bucket = [[] for i in range(len(nums)+1)]
        for key, val in count.items():
            bucket[val].append(key)
        
        output = []
        for i in range(len(bucket)-1, -1, -1):
            if k == 0:
                break
            if bucket[i]:
                for num in bucket[i]:
                    output.append(num)
                    k-=1
                    
        return output
        
        
