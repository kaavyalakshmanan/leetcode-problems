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
        
        # O(logn) time O(logn) space
        
        visit = set()
        while p:
            visit.add(p)
            p = p.parent
            
        while q:
            if q in visit:
                return q
            q = q.parent
            
        # O(logn) time O(1) space
        a, b = p, q
        
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
            
        return a
            
        
        
        
        
