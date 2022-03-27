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
        minCol, maxCol = 0, 0
        
        while q:
            currNode, currCol = q.popleft()
            minCol = min(minCol, currCol)
            maxCol = max(maxCol, currCol)
            colWise[currCol].append(currNode.val)
            if currNode.left:
                q.append((currNode.left, currCol-1))
            if currNode.right:
                q.append((currNode.right, currCol+1))
                
        return [colWise[x] for x in range(minCol, maxCol+1)]
