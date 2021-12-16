# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(max(m,n)) time O(max(m,n)+1) space
        # 2 pointers 
        
        prehead = curr = ListNode()
        carry = 0
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            currSum = val1 + val2 + carry
            
            if currSum < 10:
                carry = 0
                curr.next = ListNode(currSum)
            else: 
                carry = currSum // 10
                curr.next = ListNode(currSum % 10)
            curr = curr.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry:
            curr.next = ListNode(carry)
            
        return prehead.next 
