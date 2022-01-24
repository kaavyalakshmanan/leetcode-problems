# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(currMin, currMax, node):
            if not node:
                return True
            if node.val >= currMax or node.val <= currMin:
                return False
            return (helper(currMin, node.val, node.left) and helper(node.val, currMax, node.right))
        

        return helper(-inf, inf, root)
