# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # O(n) time since we process each node exactly twice O(1) space
        # Pointers
        
        prehead = ListNode(0, head)
        prevStart = prehead
        start = end = prehead.next 
        
        while end:
            ctr = k
            while ctr > 1 and end:
                end = end.next 
                ctr-=1
            if end:
                nextStart = end.next
                prev, curr = start, start.next
                while curr != nextStart:
                    nxt = curr.next 
                    curr.next = prev
                    prev, curr = curr, nxt
                prevStart.next = end
                prevStart = start
                start.next = nextStart
                start = nextStart
                end = start
                
            else: 
                break
                
        return prehead.next 
