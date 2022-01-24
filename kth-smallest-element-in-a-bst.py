# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Approach 1: Use array and sort
        # O(nlogn) time O(n) space
        
        def helper(node):
            if not node:
                return
            res.append(node.val)
            helper(node.left)
            helper(node.right)
        
        res = []
        helper(root)
        res.sort()
        return res[k-1]
    
        # Approach 2: Iterative Inorder Traversal
        # O(n) time O(n) space for unbalanced tree
        # O(logn) time O(logn) space for balanced tree
        
        n = 0
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n+=1
            if n == k:
                return curr.val
            curr = curr.right
                
            
        
                    


            
        
