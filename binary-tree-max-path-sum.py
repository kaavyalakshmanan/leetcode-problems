# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # This problem asks us to return the maximum sum in the binary tree under the following conditions
            # The maximum sum could either be the sum we get from splitting on a given node, aka we sum the given node and the max we get from its left and right children
            # or we dont split on the given node and instead we get the max of each path

            # O(n) time O(n) space

        globalMax = -inf

        def findMax(node):
            nonlocal globalMax


            if not node:
                return 0

            leftVal = findMax(node.left)
            rightVal = findMax(node.right)

            withoutSplit = max(node.val, node.val + leftVal, node.val + rightVal)
            withSplit = node.val + leftVal + rightVal

            globalMax = max(globalMax, withoutSplit, withSplit)

            return withoutSplit

        findMax(root)
        return globalMax



