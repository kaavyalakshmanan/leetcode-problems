# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(n) time O(1) space
        # Pointer manipulation 
        
        prehead = prev = ListNode(0, head)
        start, end = prev.next, prev.next.next if prev.next else None
        
        while end:
            temp = end.next if end else None
            start.next = temp
            end.next = start
            prev.next = end
            prev = start
            start, end = temp, temp.next if temp else None
            
        return prehead.next 
            
