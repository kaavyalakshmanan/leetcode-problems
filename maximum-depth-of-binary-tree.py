# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # O(n) time O(n) space worst case in case unbalanced tree
        # BFS

        if not root:
            return 0

        numLevels = 1
        q = collections.deque([root, None])

        while q:
            currNode = q.popleft()

            if currNode:
                if currNode.left:
                    q.append(currNode.left)

                if currNode.right:
                    q.append(currNode.right)

            else:
                if len(q) > 0:
                    numLevels +=1
                    q.append(None)

        return numLevels

       

