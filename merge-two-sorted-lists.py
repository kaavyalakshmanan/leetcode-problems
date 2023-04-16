# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # O(max(m.n)) time O(1) space
        # Pointers

        p1, p2 = list1, list2
        head = p3 = ListNode()

        while p1 and p2:
            val1 = p1.val 
            val2 = p2.val 

            if val1 <= val2:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next 
            p3 = p3.next

        if p1:
            p3.next = p1
        if p2:
            p3.next = p2

        return head.next
        
