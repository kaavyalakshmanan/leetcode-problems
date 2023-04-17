# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # O(n) time O(n) space
        
        def validate(node, minVal, maxVal):

            if not node:
                return True

            if node.val <= minVal or node.val >= maxVal:
                return False

            return validate(node.left, minVal, node.val) and validate(node.right, node.val, maxVal)

        return validate(root, -inf, inf)
