# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        res = 0
        
        def recursiveHelper(node):
            nonlocal res
            if not node:
                return
            
            if node.val > low and node.val < high:
                res+=node.val
                recursiveHelper(node.left)
                recursiveHelper(node.right)
            else:
                if node.val <= low:
                    if node.val == low:
                        res+=node.val
                    recursiveHelper(node.right)
                elif node.val >= high:
                    if node.val == high:
                        res+=node.val
                    recursiveHelper(node.left)
                
        recursiveHelper(root)
        return res
                
            
            
