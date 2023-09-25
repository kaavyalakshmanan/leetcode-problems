class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # O(n) time O(n) space
        # Bucket sort

        bucket = [[] for i in range(len(nums))]
        count = defaultdict(int)

        for n in nums:
            count[n]+=1
        
        for key, v in count.items():
            bucket[v-1].append(key)

        res = []
        for i in range(len(bucket)-1, -1, -1):
            arr = bucket[i]
            for j in range(len(arr)):
                if len(res) == k:
                    return res
                res.append(arr[j])

        return res
        
