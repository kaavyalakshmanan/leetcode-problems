# O(1) time O(capacity) space

class ListNode:

    def __init__(self, key, val):

        self.key, self.val = key, val
        self.prev, self.next  = None, None

class LRUCache:

    def __init__(self, capacity: int):

        self.cache = {}
        self.capacity = capacity

        self.head, self.tail = ListNode(-1, -1), ListNode(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def insertNode(self, node):
        tailPrev = self.tail.prev

        tailPrev.next = node
        node.prev = tailPrev

        node.next = self.tail
        self.tail.prev = node

    def deleteNode(self, node):
        nodePrev, nodeNext = node.prev, node.next

        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.deleteNode(self.cache[key])
            self.insertNode(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.deleteNode(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.insertNode(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.deleteNode(lru)

            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
