# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # O(n) time O(h) space
        # Preorder Traversal
        
        # Flattens the node tree and return the tail
        
        def preorder(node):
            if not node:
                return None
            
            # We want to return the tails so we can connect
            # The left and right subtrees get flattened
            leftTail = preorder(node.left)
            rightTail = preorder(node.right)
            
            # If both left and right subtrees are empty, we don't need to do anything
            # If right subtree is empty, we still need to move left subtree to node's right
            # If left subtree is empty, we don't need to do anything because it's already on node's right
            # Only case is left is non null
            
            if node.left:
                leftTail.right = node.right
                node.right = node.left
                node.left = None
                
            # At this point rightTail is the tail of entire flattened tree so far
            # If rightTail is empty, tail will be leftTail
            # If right subtree AND left subtree is empty, tail is going to be node
            
            last = rightTail or leftTail or node
            
            return last
            
        preorder(root)
