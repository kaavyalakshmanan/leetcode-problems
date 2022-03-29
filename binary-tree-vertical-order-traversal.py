# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # O(n) time O(n) space
        # BFS
        
        if not root:
            return []
        colWise = defaultdict(list)
        q = collections.deque([(root, 0)])
        output = []
        minCol, maxCol = 0, 0
        
        while q:
            node, col = q.popleft()
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            colWise[col].append(node.val)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
            
        return [colWise[x] for x in range(minCol, maxCol+1)]
            
