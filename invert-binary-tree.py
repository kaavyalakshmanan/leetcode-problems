# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # O(n) time O(n) space
        # Recursion
        
        if not root:
            return
        leftSubtree = root.left
        rightSubtree = root.right
        root.left = rightSubtree
        root.right = leftSubtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
