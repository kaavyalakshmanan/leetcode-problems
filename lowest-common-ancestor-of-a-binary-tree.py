# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # O(n) time O(n) space
        # BFS
        
        parents = { root: None }
        queue = collections.deque([root])
        anc = set()
        
        while p not in parents or q not in parents:
            node = queue.popleft()
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)
                
        while p:
            anc.add(p)
            p = parents[p]
        
        while q not in anc:
            q = parents[q]
            
        return q
            
            
