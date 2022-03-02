# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # O(n) time O(n) space
        
        def symmetricHelper(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            return symmetricHelper(node1.left, node2.right) and symmetricHelper(node1.right, node2.left)
        
        if not root.left and not root.right:
            return True
        return symmetricHelper(root.left, root.right)
