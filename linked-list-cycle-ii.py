# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getIntersect(head):
            slow, fast = head, head

            while fast is not None and fast.next is not None:
                slow = slow.next 
                fast = fast.next.next 
                if slow == fast:
                    return slow

            return None
        
        
        if head is None:
            return None
        intersect = getIntersect(head)
        if intersect is None:
            return None
        
        ptr1, ptr2 = head, intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next 
            ptr2 = ptr2.next 
            
        return ptr1
