# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # O(n) time O(1) space
        # Slow and fast pointers
        
        ctr = n+1
        prehead = curr = ListNode(0, head)
        slow, fast = prehead, prehead
        
        while ctr > 0:
            fast = fast.next
            ctr-=1
            
        while fast:
            fast = fast.next 
            slow = slow.next 
        
        slow.next = slow.next.next
        
        return prehead.next 
