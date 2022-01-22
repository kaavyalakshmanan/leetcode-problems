# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # O(n) time O(1) space
        # Fast and slow pointers
        
        prehead = ListNode(0, head)
        slow, fast = prehead, prehead.next
        
        while fast:
            fast = fast.next.next if fast.next else None
            slow = slow.next 
            if fast == slow:
                return True
        return False
