# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Task: Given a tree, determine if its a valid BST
        # A valid BST is such that for a given node, its left subtree is strictly smaller and its right subtree is striclty larger in value
        # No duplicates allowed
        # Algorithm: The brute force approach would be for every node, check its left subtree and right subtree and determine validity. This is an O(n) operation and we would have to repeat this n times, making it O(n^2)
        # An optimization is to do DFS and keep track of smallest and largest seen so far
        # Do that check for every node against smallest and largest
        # O(n) time O(n) space
        # DFS

        def traverseTree(node: Optional[TreeNode], small: int, large: int):
            # Base case: True case
            if not node:
                return True
            
            # Base case: False case
            if node.val <= small or node.val >= large:
                return False

            return traverseTree(node.left, small, node.val) and traverseTree(node.right, node.val, large)

        return traverseTree(root, -inf, inf)

