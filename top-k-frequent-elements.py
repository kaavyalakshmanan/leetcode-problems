class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # O(n) time O(n) space

        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num]+=1

        for key, val in count.items():
            idx = count[key]-1
            freq[idx].append(key)
        
        res = []
        j = 0

        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                if j == k:
                    return res
                res.append(n)
                j+=1

        return res


        
