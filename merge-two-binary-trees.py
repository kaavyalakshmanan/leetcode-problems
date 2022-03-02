# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # O(n) time O(n) space
        
        def mergeTreesHelper(node1, node2):
            val1, val2 = 0, 0
            if not node1 and not node2:
                return 
            if node1:
                val1 = node1.val
            if node2:
                val2 = node2.val
                
            mergedNode = TreeNode()
            mergedNode.val = val1 + val2
            mergedNode.left = mergeTreesHelper(node1.left if node1 else None, node2.left if node2 else None)
            mergedNode.right = mergeTreesHelper(node1.right if node1 else None, node2.right if node2 else None)
            
            return mergedNode
        
        return mergeTreesHelper(root1, root2)
