class Solution:
    def reverseWords(self, s: str) -> str:

        # O(n) time O(n) space

        res = []

        sArr = s.split(" ")

        for word in sArr:
            if word != "":
                res.append(word)

        res = res[::-1]]

        return " ".join(res)
