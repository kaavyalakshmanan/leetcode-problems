# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:


    def __init__(self, root: Optional[TreeNode]):
        
        # O(n) time O(n) space
        
        self.nodes = []
        self.inorderTraversal(root)
        
        self.idx = -1
        
    def inorderTraversal(self, node):
        
        # O(n) time O(n) space
        
        if not node:
            return
        self.inorderTraversal(node.left)
        self.nodes.append(node.val)
        self.inorderTraversal(node.right)
        

    def next(self) -> int:
        
        # O(n) time O(1) space
        
        self.idx +=1
        return self.nodes[self.idx]
        

    def hasNext(self) -> bool:
        
        # O(n) time O(1) space
        
        return self.idx < len(self.nodes)-1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
