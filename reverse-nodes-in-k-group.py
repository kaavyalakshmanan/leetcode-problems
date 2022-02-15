# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # O(n) time O(1) space
        
        prehead = start = end = ListNode(0, head)
        while end:
            ctr = k
            while ctr > 0:
                if not end.next:
                    break
                end = end.next 
                ctr-=1
            if ctr > 0:
                return prehead.next 
            temp = end.next 
            pA = start.next
            pB = pA.next
            pA.next = None
            while pA != end:
                pC = pB.next 
                pB.next = pA
                pA, pB = pB, pC
            startTemp = start.next 
            start.next = end
            start = startTemp
            start.next = temp
            end = start
            
        return prehead.next 
                
        
