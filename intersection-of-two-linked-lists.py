# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # O(m+n) time O(1) space
        
        m, n = 0, 0
        ptr1, ptr2 = headA, headB
        
        while ptr1:
            m+=1
            ptr1 = ptr1.next 
        ptr1 = headA
            
        while ptr2:
            n+=1
            ptr2 = ptr2.next 
        ptr2 = headB
            
        if n > m:
            m, n = n, m
            ptr1, ptr2 = ptr2, ptr1
        
        diff = m-n
        while diff > 0:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next 
            diff-=1
        
        while ptr1 or ptr2:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
            
        return None
    
        # O(m+n) time O(1) space
        # Further optimized
        
        ptr1, ptr2 = headA, headB
        while ptr1 != ptr2:
            ptr1 = headB if not ptr1 else ptr1.next 
            ptr2 = headA if not ptr2 else ptr2.next 
            
        return ptr1
            
            
