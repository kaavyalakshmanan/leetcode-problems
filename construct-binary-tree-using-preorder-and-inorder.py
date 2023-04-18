# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

                
        # Preorder traversal works like this: node, left, right
        # Aka we process current node, then we recurse down entire left subtree, then we recurse down entire right subtree

        # Inorder traversal works like this: left, node, right
        # Aka we recurse down entire left subtree, then process node, then recurse down entire right subtree

        # In order to solve this problem, it's important to understand what the preorder and inorder arrays represent and how they are related to each other
        # We just talked about what they represent, now lets talk about how they relate to each other

        # The 0th index of the preorder array always represents the current root because preorder traversal always starts at the node 
        # We now have a node to start with, lets figure out how to get the left subtree and right subtree for that node
        # In order to get the left subtree, lets first find that node in inorder, lets call that index rootIdx
        # Everything to the left of rootIdx in inorder represents the left subtree
        # To find that corresponding left subtree in preorder, we look at the subarray preorder[1:rootIdx+1]
            # We start at 1 because 0 represents the root, and we go to rootIdx+1 because that gives us exactly the left subtree in preorder
        # To find the corresponding right subtree in inorder and preorder, we look at everything to the right of rootIdx, aka pre/inorder[rootIdx+1:]

        # As with all recursive algorithms, we need a base case which will be if both preorder and inorder are null

        # O(n) time O(n) space

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        rootIdx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:rootIdx+1], inorder[:rootIdx])
        root.right = self.buildTree(preorder[rootIdx+1:], inorder[rootIdx+1:])

        return root










        
