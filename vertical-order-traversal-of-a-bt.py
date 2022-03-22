# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # O(nlogn) time O(n) space
        
        colWise = defaultdict(list)
        
        def dfs(node, row, col):
            if not node:
                return
            
            dfs(node.left, row+1, col-1)
            colWise[col].append([row, node.val])
            dfs(node.right, row+1, col+1)
            
        dfs(root, 0, 0)
        
        colWise = sorted(colWise.items())
        output = []
        
        for k, v in colWise:
            curr = []
            v = sorted(v)
            for item in v:
                curr.append(item[1])
            output.append(curr)
            
        return output 
        
        
