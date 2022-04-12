# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        # O(n) time O(n) space
        
        minVal = root.val 
        maxVal = inf
        
        def dfs(node):
            nonlocal minVal, maxVal
            if node:
                if minVal < node.val < maxVal:
                    maxVal = node.val
                elif node.val == minVal:
                    dfs(node.left)
                    dfs(node.right)
        
        dfs(root)
        return maxVal if maxVal < inf else -1
