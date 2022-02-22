# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # O(n) time O(n) space
        # Inorder traversal
        
        nodes = {}
        output = []
        
        def inorder(node, col, row):
            if not node:
                return
            
            inorder(node.left, col-1, row+1)
            if col not in nodes:
                nodes[col] = [[row, node.val]]
            else:
                nodes[col].append([row, node.val])
            inorder(node.right, col+1, row+1)
            
        inorder(root, 0, 0)
        
        nodes = sorted(nodes.items())
        for idx, val in nodes:
            curr = []
            val.sort()
            for item in val:
                curr.append(item[1])
            output.append(curr)
            
        return output 
                
                
                
                
                
