"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        # O(n) time O(1) space
        # 2 pointer
        
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        prev, curr = head, head.next 
        toInsert = False
        
        while True:
            # Case 1: insertVal belongs between min and max of list
            if prev.val <= insertVal <= curr.val:
                toInsert = True
            elif prev.val > curr.val:
                # Case 2: Either insertVal < min or insertVal > max
                # Either way, add insertVal after tail aka max
                # Prev is now pointing to the tail, aka largest elem
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True
            if toInsert:
                prev.next = Node(insertVal, curr)
                return head
            
            prev, curr = curr, curr.next 
            # Loop condition
            if prev == head:
                break
                
        # Case 3: Did not insert node in the loop (aka all node values repeat/dupes)
        prev.next = Node(insertVal, curr)
        return head
        

        
        
