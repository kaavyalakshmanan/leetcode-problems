# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # O(n) time O(n) space
        # BFS

        if not root:
            return []

        res = []

        q = [root]

        while q:
            currArr = []
            for i in range(len(q)):
                curr = q.pop(0)
                currArr.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(currArr)

        return res
