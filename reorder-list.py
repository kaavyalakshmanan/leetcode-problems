# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # O(n) time O(1) space
        # Reverse second half and merge
        
        def reverseList(head):
            if not head or not head.next:
                return head
            ptr1, ptr2 = head, head.next 
            ptr1.next = None
            while ptr2:
                ptr3 = ptr2.next
                ptr2.next = ptr1
                ptr1, ptr2 = ptr2, ptr3

            return ptr1
        
        length, curr = 0, head
        while curr:
            length+=1
            curr = curr.next
            
        length = length//2
        ptr1, ptr2 = head, head
        while length > 0:
            ptr2 = ptr2.next 
            length-=1
        ptr2 = reverseList(ptr2)
        while ptr1 != ptr2:
            temp = ptr1.next
            ptr1.next = ptr2
            ptr1 = ptr2
            ptr2 = temp
        
        return head
