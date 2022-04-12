# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        # O(nlogk) time O(H) space
        
        maxHeap = []
        q = collections.deque([root])
        
        while q:
            currNode = q.popleft()
            dist = abs(target - currNode.val) * -1
            if len(maxHeap) < k:
                maxHeap.append((dist, currNode.val))
                heapq.heapify(maxHeap)
            else:
                if dist > maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (dist, currNode.val))
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        
        res = []
        for dist, nodeVal in maxHeap:
            res.append(nodeVal)
            
        return res
