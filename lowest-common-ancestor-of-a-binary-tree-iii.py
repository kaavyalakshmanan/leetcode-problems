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
        
        # Approach 1: Use 2 Qs
        # O(logn) time O(logn) space
        
        if p.parent == q.parent:
            return p.parent
        if p.parent == q:
            return q
        if q.parent == p:
            return p
        
        pAncestors = collections.deque([])
        qAncestors = collections.deque([])
        
        while p:
            pAncestors.append(p)
            p = p.parent 
            
        while q:
            qAncestors.append(q)
            q = q.parent 
        
        while len(pAncestors) > len(qAncestors):
            pAncestors.popleft()
            
        while len(qAncestors) > len(pAncestors):
            qAncestors.popleft()
            
        while len(pAncestors) > 1:
            if pAncestors[0] == qAncestors[0]:
                return pAncestors[0]
            pAncestors.popleft()
            qAncestors.popleft()
            
        return pAncestors[0]

        # Approach 2: No additional space
        # O(logn) time, O(1) space
        
        a, b = p, q
        
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
            
        return a
