class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # O(n*4^n) time O(n) space
        # Backtracking 
        
        letterDict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []

        def backtracking(idx, currStr):
            if idx == len(digits):
                res.append(currStr)
                return

            for letter in letterDict[digits[idx]]:
                backtracking(idx+1, currStr+letter)


        if digits:
            backtracking(0, "")
        return res
