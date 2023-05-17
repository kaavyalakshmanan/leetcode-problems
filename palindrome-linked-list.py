# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # O(n) time O(n) space

        length = 0
        curr = head

        while curr:
            length+=1
            curr = curr.next
        
        isOdd = False
        if length % 2:
            isOdd = True

        length = length//2
        curr = head
        stack = []

        while length > 0:
            stack.append(curr.val)
            curr = curr.next
            length-=1
        
        if isOdd:
            curr = curr.next

        while curr:
            if curr.val != stack[-1]:
                return False
            stack.pop()
            curr = curr.next

        return True

        
