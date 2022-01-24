# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # O(logn) time O(logn) space for balanced tree
        # O(n) time O(N) space for unbalanced tree
        # Approach 1: Binary Search
        
        if (root.val >= p.val and root.val <= q.val) or (root.val >= q.val and root.val <= p.val):
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # Approach 2: Iterative
        curr = root
        while curr:
            if (curr.val >= p.val and curr.val <= q.val) or (curr.val >= q.val and curr.val <= p.val):
                return curr
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
        
        
        
        
        
        
