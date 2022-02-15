class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # O(n*4^n) time O(n) space
        # Backtracking 
        
        digitsToLetters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        def backtracking(idx, currLetters):
            if idx == len(digits):
                output.append(currLetters)
                return
            
            for c in digitsToLetters[digits[idx]]:
                backtracking(idx+1, currLetters+c)
            
        output = []
        if digits:
            backtracking(0, "")
        return output
            
            
        
