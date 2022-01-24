# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Approach 1: Iterative (BFS)
        # O(n) time O(n) space
        
        if not root:
            return []
        q = collections.deque([root])
        output = []
        
        while q:
            qLen = len(q)
            currNodes = []
            for i in range(qLen):
                curr = q.popleft()
                currNodes.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            output.append(currNodes)
            
        return output 
    
        # Approach 2: Recursive 
        # O(n) O(n) space
        
        output = []
        
        def helper(node, idx):
            if not node:
                return
            if idx == len(output):
                output.append([])
            output[idx].append(node.val)
            helper(node.left, idx+1)
            helper(node.right, idx+1)
        
        helper(root, 0)
        return output 
        
