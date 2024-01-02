class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # O(n) time O(n) space
        # Bucket sort
        
        bucket = [[] for i in range(len(nums))] 

        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        
        for key, val in count.items():
            bucket[val-1].append(key)
        
        res = []
        for l in bucket[::-1]:
            for item in l:
                res.append(item)
                if len(res) == k:
                    return res

        return res

