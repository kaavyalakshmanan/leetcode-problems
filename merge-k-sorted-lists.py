# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Approach 1: Min Heap
        # O(n*logk) time O(k) space where k = len(lists) and n = len(each list)
        
        heap = [ (l.val, i) for i, l in enumerate(lists) if l ]
        heapq.heapify(heap)
        prehead = curr = ListNode()
        
        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next 
            
            node = lists[idx] = lists[idx].next 
            if node:
                heapq.heappush(heap, (node.val, idx))
                
        return prehead.next
        
        # Approach 2: Divide & Conquer
        # O(n*logk) time O(1) space where n = len(lists) and k = len(each list)
        
        def mergeTwoSortedLists(list1, list2):
        
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
        
        if not lists:
            return None
        while len(lists) >= 2:
            mergedList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedList.append(mergeTwoSortedLists(list1, list2))
            lists = mergedList
            
        return lists[0]
                
            
