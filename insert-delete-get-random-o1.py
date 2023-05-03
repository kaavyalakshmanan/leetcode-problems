class RandomizedSet:

    # O(1) time for everything

    def __init__(self):

        # map val to idx in arr
        self.dict = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.arr.append(val)
            self.dict[val] = len(self.arr)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:

        if val not in self.dict:
            return False
        idx = self.dict[val]
        self.arr[idx] = self.arr[-1]
        self.dict[self.arr[idx]] = idx
        self.arr.pop()
        del self.dict[val]
        
        return True
        

    def getRandom(self) -> int:
        idx = randrange(len(self.arr))
        return self.arr[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
