class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # O(n) time O(n) space
        # Backstracking
        
        res = []

        def backtracking(numOpen, numClose, currStr):

            # base case
            if numOpen == n and numClose == n:
                res.append(currStr)
                return 

            # general case
            if numOpen < n:
                backtracking(numOpen+1, numClose, currStr+"(")
            if numClose < numOpen:
                backtracking(numOpen, numClose+1, currStr+")")

        backtracking(0, 0, "")

        return res
