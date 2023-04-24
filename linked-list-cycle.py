# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Approach 1: Use a set
        # O(n) time O(n) space

        nodes = set()
        ptr = head

        while ptr:
            if ptr in nodes:
                return True
            nodes.add(ptr)
            ptr = ptr.next

        return False

        # Approach 2: Floyds cycle finding algo without auxiliary space

        # O(n) time O(1) space
        prehead = ListNode()
        prehead.next = head
        slow, fast = prehead, prehead.next
        ctr = 1

        while fast:
            if fast == slow:
                return True
            if not ctr % 2:
                slow = slow.next
            fast = fast.next
            ctr+=1

        return False
