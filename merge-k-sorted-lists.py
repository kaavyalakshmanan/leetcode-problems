# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # # Approach 1: Use a minHeap
        # # O(nlogk) time O(n) space

        # minHeap = [(l.val, idx) for idx, l in enumerate(lists) if l]
        # heapq.heapify(minHeap)
        # p3 = head = ListNode()

        # while len(minHeap) > 0:
        #     curr, idx = heapq.heappop(minHeap)
        #     p3.next = ListNode(curr)
        #     p3 = p3.next 

        #     node = lists[idx] = lists[idx].next 
        #     if node:
        #         heapq.heappush(minHeap, (node.val, idx))

        
        # return head.next

        # Approach 2: Reduce this problem to Merge 2 Sorted Lists
        # O(nlogk) time O(1) space

        while len(lists) > 1:
            res = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None

                mergedList = self.mergeTwoSortedLists(list1, list2)
                res.append(mergedList)
            lists = res

        return lists[0] if len(lists) > 0 else None

    def mergeTwoSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        p3 = head = ListNode()
        p1, p2 = list1, list2

        while p1 and p2:
            val1 = p1.val 
            val2 = p2.val

            if val1 <= val2:
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




            
