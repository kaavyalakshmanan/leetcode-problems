# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(min(m,n)) time O(1) space
        # 2 pointers
        
        prehead = curr = ListNode()
        
        while list1 and list2:
            val1 = list1.val
            val2 = list2.val 
            
            if val1 <= val2:
                curr.next = list1 
                list1 = list1.next if list1 else None
            else:
                curr.next = list2 
                list2 = list2.next if list2 else None
            curr = curr.next
            
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return prehead.next
