class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Backtracking
        
        def backtracking(numLeft, numRight, currStr):
            if numLeft == 0 and numRight == 0:
                output.append(currStr)
                return
            if numLeft > 0:
                backtracking(numLeft-1, numRight, currStr+"(")
            if numLeft < numRight:
                backtracking(numLeft, numRight-1, currStr+")")
            
        output = []
        backtracking(n, n, "")
        return output 
