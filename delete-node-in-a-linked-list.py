# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # O(n) time O(1) space

        curr, nxt = node, node.next 
        while curr:
            curr.val = nxt.val
            if not nxt.next:
                curr.next = None
            curr = curr.next
            nxt = nxt.next 

