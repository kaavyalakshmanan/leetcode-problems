"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        # # O(n) time O(n) space
        # # Level order traversal aka bfs
        # # The reason space complexity is O(n) is because since this is a perfect binary tree that means each node has exactly 2 children, so the number of leaf nodes will be n/2 whch is O(n)

        # if not root:
        #     return None

        # q = collections.deque([root, None])

        # while q:
        #     currNode = q.popleft()
        #     if currNode:
        #         if q[0] is not None:
        #             currNode.next = q[0]
        #         else:
        #             currNode.next = None
        #         if currNode.left:
        #             q.append(currNode.left)
        #             if currNode.right:
        #                 q.append(currNode.right)
        #     else:
        #         if q:
        #             q.append(None)

        # return root

        # now lets address the follow-up
        # we want to use comnstant memory 
        # level order traversal (bfs) is still the best approach, however we cant use the q
        # maybe we can simulate the q with pointers
        # O(n) time O(1) space

        # heres how this algorithm works:
            # we use 2 pointers, curr and nxt where curr is initialized to the root and nxt is initialized to root.left
            # for every curr, we connect its left and right children
            # if it has a next, we connect its right child with its next's left child
                # then we move to the next
                # when we do this, we're connecting the nodes for a given level
            # if it doesnt have a next, we move curr to nxt (not to be confused with next) and we move nxt to curr's left
                # when we do this, we are going to the very beginning of the new level
                # nxt will ALWAYS point to the leftmost node of a given level
            # so when we connect all the nodes of a given level, eventually since curr keeps moving to curr.next, it will be null (aka end of level)
            # so thats why when we move curr back to nxt, we're moving curr to the start of the next level
            # and when we move nxt to curr.left, we're getting ready for the level after
            # so eventually curr will be a leaf node and wont have a left, so nxt will be null
            # thats the temrination condition

        curr, nxt = root, root.left if root else None

        while nxt:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next 
            if not curr:
                curr = nxt
                nxt = curr.left

        return root

        


