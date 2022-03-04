"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # O(n) time O(n) space
        
        nodes = {}
        ptr1 = head
        ptr2 = copyHead = Node(0, None, None)
        
        while ptr1:
            ptr2.next = Node(ptr1.val, None, None)
            ptr2 = ptr2.next 
            nodes[ptr1] = ptr2
            ptr1 = ptr1.next 
            
        ptr1 = head
        while ptr1:
            ptr2 = nodes[ptr1]
            ptr2.next = nodes[ptr1.next] if ptr1.next else None
            ptr2.random = nodes[ptr1.random] if ptr1.random else None
            ptr1 = ptr1.next 
            
        return copyHead.next 
