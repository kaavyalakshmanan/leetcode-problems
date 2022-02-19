class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # O(n*t) time O(n*t) space
        # DP + Backtracking
        
        dp = {} # mappig (idx, totalSoFar) -> count if we start at that idx with that totalSoFar
        
        def backtrack(idx, totalSoFar):
            if idx == len(nums):
                return 1 if totalSoFar == target else 0
            if (idx, totalSoFar) in dp:
                return dp[(idx, totalSoFar)]
           
            dp[(idx, totalSoFar)] = backtrack(idx+1, totalSoFar + nums[idx]) + backtrack(idx+1, totalSoFar - nums[idx])
            
            return dp[(idx, totalSoFar)]
        
        return backtrack(0, 0)
        
                
