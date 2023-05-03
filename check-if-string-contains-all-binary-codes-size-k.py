class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        # this problem is actually a lot simpler than it seems
        # rather than generating every possible binary code of length k and then checking if it exists as a substring in s, we can just iterate over s, compute every possible substring of length k, add to a set, then in the end check if length of set is 2^k

        # O(n*k) time O(2^k) space

        if len(s) < k:
            return False

        left, right = 0, k-1
        codes = set()

        while right < len(s):
            codes.add(s[left:right+1])
            left+=1
            right+=1

        return len(codes) == (2 ** k)

