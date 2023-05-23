class Solution:
    def reverseVowels(self, s: str) -> str:

        # O(n) time O(1) space because number of vowels is constant 

        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowelDict = defaultdict(int)
        vowelArr = []

        for i, c in enumerate(s):
            char = c.lower()
            if char in vowels:
                vowelDict[i] = c
                vowelArr.append(c)

        res = ""
        for i, c in enumerate(s):
            if i in vowelDict:
                res += vowelArr[-1]
                vowelArr.pop()
            else:
                res += c

        return res
