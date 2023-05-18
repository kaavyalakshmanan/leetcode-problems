# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # O(n) time O(n) space
        
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            if curr.val == val and not prev:
                curr.next = None
                head = nxt
                curr = nxt
            elif curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt

        return head
