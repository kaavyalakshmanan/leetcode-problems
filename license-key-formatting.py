class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        i = len(s)-1
        res = [[]]
        while i >= 0:
            c = s[i]
            if c != '-':
                if len(res[-1]) == k:
                    res.append([])
                res[-1].append(c.upper())

            i-=1

        res = res[::-1]
        ans = ""
        for l in res:
            l = l[::-1]
            ans += "".join(l)
            ans += "-"

        return ans[:-1]
