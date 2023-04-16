class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # O(m+n) time O(m) space
        # KMP Algo
        
        # Step 1: lps (longest prefix suffix)

        lps = [0] * len(needle)
        prev, curr = 0, 1
        while curr < len(needle):
            if needle[prev] == needle[curr]:
                lps[curr] = prev+1
                prev, curr = prev+1, curr+1
            elif prev > 0:
                prev = lps[prev-1]
            else:
                curr+=1

        # Step 2: Use lps to find index
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i+1, j+1
            elif j > 0:
                j = lps[j-1]
            else:
                i+=1

            if j == len(needle):
                return i-(len(needle))

        return -1


