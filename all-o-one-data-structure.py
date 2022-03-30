class Node:
    
    def __init__(self, key, val):
        
        self.key = key
        self.val = val
        
        self.prev, self.next = None, None
        
    def __str__(self):
        return f"({self.key}, {self.val})"
    

class AllOne:

    def __init__(self):
        
        self.head = Node("", inf)
        self.tail = Node("", -inf)
        
        self.head.next = self.tail
        self.tail.prev = self.head 
        
        self.stringCount = {}
    
    # Insering a NEW node
   
    def insertNode(self, node):
        tailPrev = self.tail.prev 
        tailPrev.next = node
        node.prev = tailPrev
        node.next = self.tail
        self.tail.prev = node
    
    # Delete EXISTING node
    def delNode(self, node):
        prevNode, nextNode = node.prev, node.next 
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
        del node
    
    # Swap EXISTING node
     # h -> (l, 1) -> t
    def swapNode(self, node):
        prevNode, nextNode = node.prev, node.next 
        
        # head ->  -> (hello, 3) -> (leet, 2) -> tail
        # Swap left
        if node.val > prevNode.val:
            leftNeighbor = prevNode.prev
            leftNeighbor.next = node
            node.prev = leftNeighbor 
            node.next = prevNode
            prevNode.prev = node
            
            prevNode.next = nextNode
            nextNode.prev = prevNode
            
        # Swap right
        elif node.val < nextNode.val:
            rightNeighbor = nextNode.next
            rightNeighbor.prev = node
            node.next = rightNeighbor 
            node.prev = nextNode
            nextNode.next = node
            
            prevNode.next = nextNode
            nextNode.prev = prevNode
            
        
        

    def inc(self, key: str) -> None:
        
        print(self.stringCount)
        
        if key in self.stringCount:
            self.stringCount[key].val+=1
            self.swapNode(self.stringCount[key])
        
        else:
            self.stringCount[key] = Node(key, 1)
            self.insertNode(self.stringCount[key])
            
        
        

    def dec(self, key: str) -> None:
        
        self.stringCount[key].val-=1
        
        # Remove node
        if self.stringCount[key].val == 0:
            self.delNode(self.stringCount[key])
            del self.stringCount[key]
        
        else:
            self.swapNode(self.stringCount[key])
        

    def getMaxKey(self) -> str:
        
        return self.head.next.key
        

    def getMinKey(self) -> str:
        
        return self.tail.prev.key
        

#         ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "dec", "dec", "getMinKey"]
        
#         {
#             hello: Node(hello, 3),
#             leet: Node(leet, 2)
#             dog: Node(dog, 1)
#         }
        
#         head -> Node(hello, 3) -> Node(leet, 4) -> tail
#         tail
        
#         maxVal = (hello, 2)
#         minVal = (hello, 1)
        
       

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
