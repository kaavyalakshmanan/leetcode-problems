# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(n) time O(1) space
        # 3 pointers
        
        if not head or not head.next:
            return head
        ptr1, ptr2 = head, head.next 
        ptr1.next = None
        while ptr2:
            ptr3 = ptr2.next
            ptr2.next = ptr1
            ptr1, ptr2 = ptr2, ptr3
            
        return ptr1
