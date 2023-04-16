class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # Backtracking 
        
        res = []

        def backtracking(numOpen, numClose, currStr):
            # Base Case True
            if numOpen == n and numClose == n:
                res.append(currStr)
                return 
            
            # When do we put down open
            if numOpen < n:
                backtracking(numOpen+1, numClose, currStr+"(")
            
            # When do we put down close
            if numOpen > numClose:
                backtracking(numOpen, numClose+1, currStr+")")




        backtracking(0, 0, "")
        return res
