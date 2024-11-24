# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # O(max((n+m))) time O(1) space
        # 2 pointers

        p1, p2 = list1, list2
        head = ListNode()
        curr = head
        while p1 or p2:
            val1 = p1.val if p1 else inf
            val2 = p2.val if p2 else inf
            if val1 <= val2:
                nextPtr = p1.next
                curr.next = p1
                p1 = nextPtr
            else:
                nextPtr = p2.next
                curr.next = p2
                p2 = nextPtr
            curr = curr.next

        return head.next

        
        
