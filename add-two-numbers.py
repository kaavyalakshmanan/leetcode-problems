# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # O(max(m,n)) time O(max(m.n)+1) space
        # 2 pointers
        
        head = ListNode()
        p1, p2, p3 = l1, l2, head
        carry = 0

        while p1 or p2:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            currSum = val1 + val2 + carry

            if currSum < 10:
                p3.next = ListNode(currSum)
                if carry > 0:
                    carry = 0
            else:
                p3.next = ListNode(currSum % 10)
                carry = currSum // 10
            p3 = p3.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        if carry:
            p3.next = ListNode(carry)

        return head.next 
