# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []

        colTable = defaultdict(list)
        minCol = maxCol = 0
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node is not None:
                colTable[col].append(node.val)
                minCol = min(minCol, col)
                maxCol = max(maxCol, col)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
        
       
        return [colTable[x] for x in range(minCol, maxCol + 1)]
