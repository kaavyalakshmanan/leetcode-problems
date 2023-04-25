class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        # O(n) time O(1) space

        res = 0
        exp = 0

        for i in range(len(columnTitle)-1, -1, -1):
            diff = ((ord(columnTitle[i].lower())) - ord('a')) + 1
            diff *= (26 ** exp)
            res += diff
            exp+=1


        return res

