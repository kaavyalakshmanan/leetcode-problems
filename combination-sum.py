class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # O(2^n) time O(n) space
        # Backtracking 
        
        def backtrack(idx, currSum, currNums):
            if currSum == target:
                output.append(currNums.copy())
                return
            if idx == len(candidates) or currSum > target:
                return
            
            currNums.append(candidates[idx])
            backtrack(idx, currSum + candidates[idx], currNums)
            currNums.pop()
            backtrack(idx+1, currSum, currNums)
            
        
        
        output = []
        backtrack(0, 0, [])
        return output
