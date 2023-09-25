class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # O(n*m) time O(n*m) space
        # Frequency counter of chars
        
        res = defaultdict(list)

        for w in strs:
            chars = [0] * 26
            for c in w:
                chars[ord(c) - ord('a')]+=1
            res[tuple(chars)].append(w)

        return res.values()
