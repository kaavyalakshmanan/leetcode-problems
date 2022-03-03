# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # O(n) time O(n) space
        # Reverse second half of list 
        
        ptr1, ptr2 = head, head
        length = 0
        
        while ptr2:
            length+=1
            ptr2 = ptr2.next 
        
        mid = length//2
        ptr2 = head
        
        while mid > 0:
            ptr2 = ptr2.next 
            mid-=1
            
        ptr3 = ptr2.next 
        ptr2.next = None
        while ptr3:
            temp = ptr3.next 
            ptr3.next = ptr2
            ptr2, ptr3 = ptr3, temp
            
        while ptr1 != ptr2 and ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next 
            ptr2 = ptr2.next
            
        return True
