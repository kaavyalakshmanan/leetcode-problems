class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        # O(n) time O(n) space
        
        count = {}
        for word in words:
            count[word] = 1 + count.get(word, 0)
            
        bucket = [[] for i in range(len(words)+1)]
        
        for key, val in count.items():
            bucket[val].append(key)
            
        res = []
        for i in range(len(bucket)-1, -1, -1):
            if not bucket[i]:
                continue
            arr = sorted(bucket[i])
            for item in arr:
                res.append(item)
                if len(res) == k:
                    return res
