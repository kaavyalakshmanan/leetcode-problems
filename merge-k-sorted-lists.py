# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # O(nlogk) time O(n) space where k = length of lists and n = number of nodes in each list
        
        # Approach 1: Min heap
        heap = [(l.val, i) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)
        prehead = ptr = ListNode()
        
        while heap:
            curr, idx = heapq.heappop(heap)
            ptr.next = ListNode(curr)
            ptr = ptr.next
            
            node = lists[idx] = lists[idx].next 
            if node:
                heapq.heappush(heap, (node.val, idx))
                
        return prehead.next 
    
        # Approach 2: Divide & Conquer
        def mergeTwoLists(list1, list2):
            prehead = curr = ListNode()
            while list1 and list2:
                val1 = list1.val 
                val2 = list2.val 
                if val1 <= val2:
                    curr.next = list1
                    list1 = list1.next 
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            if list1:
                curr.next = list1
            elif list2:
                curr.next = list2

            return prehead.next 
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                
                mergedLists.append(mergeTwoLists(list1, list2))
            lists = mergedLists
            
        return lists[0] if lists else None
        
