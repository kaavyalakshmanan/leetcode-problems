"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        # O(logn) time O(1) space
        # 2 pointers
        
        pPtr, qPtr = p, q
        ctr = 0
        while pPtr != qPtr:
            ctr+=1
            pPtr = pPtr.parent if pPtr.parent else q
            qPtr = qPtr.parent if qPtr.parent else p
            
        print(ctr)
        return pPtr
