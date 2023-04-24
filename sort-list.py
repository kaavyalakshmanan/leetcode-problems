# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # The problem description tells us to solve it in O(nlogn) which implies making use of a sorting algo like merge sort or quick sort
        # O(nlogn) time O(n) space because recursion

        # base case
        if not head or not head.next:
            return head

        # split list into 2 halves
        left, right = head, self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        leftHalf = self.sortList(left)
        rightHalf = self.sortList(right)

        return self.mergeTwoSortedLists(leftHalf, rightHalf)

    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeTwoSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        p3 = head = ListNode()

        while p1 and p2:
            if p1.val <= p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next 

        if p1:
            p3.next = p1
        if p2:
            p3.next = p2

        return head.next

        

        

  

