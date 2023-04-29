class Node:
    def __init__(self, key: int, val: int, next: None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    # we want to design a hashmap class without using built-in hashmaps (aka {})
    # since we will have at most 1000 calls to our class, lets initialize an array of size 1000
    # given an arbitrary key, we mod it by 1000 to find the appropriate array index it belongs in
    # but we could have multiple keys map to the same index since we are modding
    # the solution: chaining
    # each array index will contain a linkedlist where each node contains a key, val pair
    # so we add a new key as a node to that linked list
    # and if we want to retrieve or remove or update, we can easily do that in the linked list

    # O(1) time O(n) space

    def __init__(self):

        self.arr = [ Node(-1, -1, None) for i in range(1000) ] 

    def hash(self, key: int) -> int:
        return key % (len(self.arr))
        

    # O(n) time O(1) space
    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        curr = self.arr[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        
        curr.next = Node(key, value, None)
        

    # O(n) time O(1) space
    def get(self, key: int) -> int:
        idx = self.hash(key)
        curr = self.arr[idx]

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        
        return -1
        

    # O(n) time O(1) space
    def remove(self, key: int) -> None:
        idx = self.hash(key)
        curr = self.arr[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return 
            curr = curr.next
        
      
        
       
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
