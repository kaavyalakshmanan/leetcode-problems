class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Backtracking with DFS
        # O(n*2^n)

        res = []
        subset = []

        def dfs(idx):

            # Base case
            if idx == len(nums):
                res.append(subset.copy())
                return 

            # At every point in the decision tree, we have 2 decisions
            # Decision 1: Choose to include nums[idx]
            subset.append(nums[idx])
            dfs(idx+1)

            # Decision 2: Dont include nums[idx]
            subset.pop()
            dfs(idx+1)


        dfs(0)
        return res
