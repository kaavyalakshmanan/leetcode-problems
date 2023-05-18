# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Use a BFS algo to iterate over tree, using a q
        # Also make use of a parents dict where key = node and val = node's parent
        # Also make use of an anc set to find the LCA
        # O(n) time O(n) space

        # Step 1: BFS until both p and q are in parents dict
        parents = { root: None }
        queue = collections.deque([root])

        while p not in parents or q not in parents:
            node = queue.popleft()
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)

        # Step 2: Put all of p's ancestors in anc
        anc = set()
        while p:
            anc.add(p)
            p = parents[p]
        
        # Step 3: Search for q's ancestor in anc
        while q not in anc:
            q = parents[q]

        return q
            


