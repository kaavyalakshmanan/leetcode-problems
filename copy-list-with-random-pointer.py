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

        # Use a hashmap to solve this problem

        # O(n) time O(n) space

        nodes = {}
        prehead = Node(0)
        p1, p2 = head, prehead

        while p1:
            if p1 not in nodes:
                p2.next = Node(p1.val)
                nodes[p1] = p2.next
            else:
                p2.next = nodes[p1]
            if p1.random:
                if p1.random not in nodes:
                    nodes[p1.random] = Node(p1.random.val)
                nodes[p1].random = nodes[p1.random]
            p1 = p1.next
            p2 = p2.next

        return prehead.next 

