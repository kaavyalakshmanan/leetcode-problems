class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # O(n*m) time O(n*m) space
        # Frequency count

        res = defaultdict(list)

        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')]+=1
            res[tuple(count)].append(w)

        return res.values()
        
