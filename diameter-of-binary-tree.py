# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # O(n) time O(n) space
        # DFS
        
        globalMax = 0
        
        def dfs(node):
            nonlocal globalMax
            if not node:
                return 0
            
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            
            
            globalMax = max(globalMax, leftPath + rightPath)
            
            return max(leftPath, rightPath) + 1
        
        dfs(root)
        return globalMax
