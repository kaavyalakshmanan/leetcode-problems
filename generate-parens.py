class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Backtracking
        
        def backtrack(left, right, curr):
            if left == 0 and right == 0:
                output.append(curr)
                return
            if left > 0:
                backtrack(left-1, right, curr+"(")
            if left < right:
                backtrack(left, right-1, curr+")")
                
        output = []
        backtrack(n, n, "")
        return output
