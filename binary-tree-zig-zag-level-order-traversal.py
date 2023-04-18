# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # O(n) time O(n) space worst case in case unbalanced tree
        # BFS

        res = []
        currArr = deque()

        if root is None:
            return res

        q = deque([root, None])
        startLeft = True
        

        while len(q)>0:
            currNode = q.popleft()

            if currNode:
                if startLeft:
                    currArr.append(currNode.val)
                else:
                    currArr.appendleft(currNode.val)

                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)

            else:
                res.append(currArr)
                if len(q) > 0:
                    q.append(None)

                currArr = deque()
                startLeft = not startLeft

        return res
