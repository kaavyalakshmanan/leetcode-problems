# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        # O(n) time O(n) space
        # Prefix Sum
        
        globalCount, globalSum = 0, 0
        prefixSum = { 0: 1 }
        
        def preorderTraversal(node):
            nonlocal globalSum
            nonlocal globalCount
            
            if not node:
                return
            
            globalSum += node.val
                
            if globalSum - targetSum in prefixSum:
                globalCount += prefixSum[globalSum - targetSum]
                
            prefixSum[globalSum] = 1 + prefixSum.get(globalSum, 0)
            
            preorderTraversal(node.left)
            preorderTraversal(node.right)
            
            if globalSum in prefixSum:
                prefixSum[globalSum] -= 1
            globalSum -= node.val
        
        
        
        preorderTraversal(root)
        return globalCount
