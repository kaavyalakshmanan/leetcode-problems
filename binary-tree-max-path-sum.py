# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxIfWeSplit = root.val
        
        def helper(node):
            nonlocal maxIfWeSplit
            if not node:
                return 0
            leftVal = helper(node.left)
            rightVal = helper(node.right)
            maxIfWeDontSplit = max(node.val + leftVal, node.val + rightVal, node.val)
            maxIfWeSplit = max(maxIfWeSplit, leftVal+rightVal+node.val, maxIfWeDontSplit)
            return maxIfWeDontSplit
        
        helper(root)
        return maxIfWeSplit        
