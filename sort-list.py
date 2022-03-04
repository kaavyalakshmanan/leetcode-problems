# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # MergeSort --> divide and conquer 
        # O(nlogn) time O(logn) space
        
        # Base case
        if not head or not head.next:
            return head
        
        # Split the list in half
        # Left points to first list, right points to second list
        left = head
        right = self.getMid(left)
        tmp = right.next
        right.next = None
        right = tmp
        
        # Recurse on both left and right halves of list
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge left and right
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
        return slow
    
    # Merge two sorted linked lists
    def merge(self, left, right):
        dummy = ptr = ListNode()
        while left or right:
            leftVal, rightVal = left.val if left else inf, right.val if right else inf
            if leftVal <= rightVal:
                ptr.next = left
                left = left.next if left else None
            else:
                ptr.next = right
                right = right.next if right else None
            ptr = ptr.next
            
        return dummy.next
        
            
            
            
        
        
