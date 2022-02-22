# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # O(n) time O(d) space where d is the max number of nodes at a given level
        # BFS
        
        if not root:
            return []
        q = collections.deque([root])
        output = []
        
        while q:
            output.append(q[-1].val)
            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
        return output 
            
