# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # O(n+m) time O(1) space

        if not headA or not headB:
            return 0

        lenA, lenB = 0, 0
        pA, pB = headA, headB

        while pA:
            lenA+=1
            pA = pA.next
        while pB:
            lenB+=1
            pB = pB.next

        pA, pB = headA, headB

        # Helper function moves corresponding LL pointer so starting at same pos
        if lenA > lenB:
            pA = self.getStartingPos(pA, lenA-lenB)
        elif lenB > lenA:
            pB = self.getStartingPos(pB, lenB-lenA)
        
        while pA and pB:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
        
        return None

    def getStartingPos(self, ptr: ListNode, diff: int) -> Optional[ListNode]:

        while diff > 0:
            ptr = ptr.next
            diff-=1

        return ptr


