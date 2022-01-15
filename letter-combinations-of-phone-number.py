class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # O(n*4^n) time O(n) space
        # Backtracking 
        
        def backtrack(idx, curr):
            if idx == len(digits):
                output.append(curr)
                return
            
            currLetters = letters[digits[idx]]
            for c in currLetters:
                backtrack(idx+1, curr+c)
        
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        output = []
        if not digits:
            return output
        backtrack(0, "")
        return output 
